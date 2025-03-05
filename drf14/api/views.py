from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from api.models import Student
from api.serilaizer import StudentSerializer

"""ModelViewSet"""
# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

"""ReadOnlyModelViewSet"""
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer