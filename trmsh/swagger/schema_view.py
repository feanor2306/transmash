import warnings
from urllib.parse import urljoin

from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import OpenAPIRenderer
from rest_framework.schemas.openapi import SchemaGenerator
from rest_framework.views import APIView

from rest_framework_swagger.settings import swagger_settings
from rest_framework_swagger.views import get_swagger_view

import yaml



class MyOpenAPIRenderer(OpenAPIRenderer):
    def render(self, data, media_type=None, renderer_context=None):
        class Dumper(yaml.Dumper):
            def ignore_aliases(self, data):
                return True

        return yaml.dump(data, default_flow_style=False, sort_keys=False, Dumper=Dumper).encode('utf-8')


class CustomSchema(SchemaGenerator):
    def get_schema(self, request=None, public=False):
        self._initialise_endpoints()
        components_schemas = {}

        # Iterate endpoints generating per method path operations.
        paths = {}
        _, view_endpoints = self._get_paths_and_endpoints(None if public else request)
        for path, method, view in view_endpoints:
            if not self.has_view_permissions(path, method, view):
                continue

            operation = view.schema.get_operation(path, method)
            # if settings.DEBUG:
            #     print(">> ", path, method)
            components = view.schema.get_components(path, method)
            for k in components.keys():
                if k not in components_schemas:
                    continue
                if components_schemas[k] == components[k]:
                    continue
                warnings.warn('Schema component "{}" has been overriden with a different value.'.format(k))

            components_schemas.update(components)

            # Normalise path for any provided mount url.
            if path.startswith('/'):
                path = path[1:]
            path = urljoin(self.url or '/', path)

            if self.is_secure_view(view):
                operation["security"] = swagger_settings.SECURITY_DEFINITIONS

            paths.setdefault(path, {})
            paths[path][method.lower()] = operation

        self.check_duplicate_operation_id(paths)

        # Compile final schema.
        schema = {
            'openapi': '3.0.2',
            'info': self.get_info(),
            'paths': paths,
        }

        if len(components_schemas) > 0:
            schema['components'] = {
                'schemas': components_schemas
            }

        return schema

    def is_secure_view(self, view: APIView) -> bool:
        permission_classes = getattr(view, "permission_classes", None)
        if not permission_classes:
            return False

        for _permission_class in permission_classes:
            if _permission_class == IsAuthenticated or issubclass(_permission_class, IsAuthenticated):
                return True

        return False


schema_view = get_swagger_view(title='API')
