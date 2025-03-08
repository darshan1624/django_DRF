from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from api.models import Student
from api.serializer import StudentSerialzier

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzier