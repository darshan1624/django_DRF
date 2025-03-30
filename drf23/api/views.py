from django.shortcuts import render
from api.models import Student
from api.serializer import StudentSerializer 
from api.customized_pagination import MyPageNumberPagination, MyLimitOffsetPagination, MyCursorPagination

# Create your views here.
from rest_framework.generics import ListAPIView

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyCursorPagination
