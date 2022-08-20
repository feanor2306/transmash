from django.contrib import admin
from django.contrib import admin

from .models import *

# class EmployeeAdmin(admin.ModelAdmin):
#   list_display = ('id', 'name', 'photo')
## search_fields = ('name',)


admin.site.register(Employee)
admin.site.register(Skills)
admin.site.register(Branches)
admin.site.register(Personal)

# Register your models here.

# Register your models here.
def site():
    return None