from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from api.models import Student
from api.serializer import StudentSerialzier
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from api.custom_permission import CustomPermission

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzier

    authentication_classes = [SessionAuthentication]
    permission_classes = [CustomPermission]