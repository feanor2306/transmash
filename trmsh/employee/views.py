from django.forms import model_to_dict
from django.shortcuts import render
from pip._internal import req
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from .models import *
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


    # @action(methods=['get'], detail=False)
    # def get_seniority(self, request):
    #     seni = Seniority.objects.all()
    #     return Response({'seniority': [s.name for s in seni]})

# class EmployeeAPIList(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
# class EmployeeAPIUpdate(generics.UpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#
# class EmployyAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class EmployeeAPIView(APIView):
#     def get(self, request):
#         w = Employee.objects.all()
#         return Response({'entry': EmployeeSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'entry': serializer.data})
#
#     # def put(self, request, *args, **kwargs):
#     #     pk = kwargs.get('pk', None)
#     #     if not pk:
#     #         return Response({'error': "Method PUT not allowed"})
#
#         try:
#             instance = Employee.objects.get(pk=pk)
#         except:
#             return Response({'error': "Object does not exist"})
#         serializer = EmployeeSerializer(instance=instance,  data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'entry': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": 'Method DELETE not allowed'})
#
#         try:
#             instance = Employee.objects.get(pk=pk)
#         except:
#             serializer = EmployeeSerializer(instance=instance, data=request.data)
#             serializer.is_valid(raise_exception=True)



#class EmployeeAPIView(generics.ListAPIView):
 #   queryset = Employee.objects.all()
  #  serializer_class = EmployeeSerializer
