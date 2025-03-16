from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from api.models import Student
from api.serializer import StudentSerialzier
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzier
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


