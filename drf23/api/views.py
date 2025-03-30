from django.shortcuts import render
from api.models import Student
from api.serializer import StudentSerializer 

# Create your views here.
from rest_framework.generics import ListAPIView

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

