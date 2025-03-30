from django.shortcuts import render
from api.models import Student
from api.serializer import StudentSerializer 

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['passby', 'city']

