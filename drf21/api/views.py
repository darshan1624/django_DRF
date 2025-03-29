from django.shortcuts import render
from api.models import Student
from api.serializer import StudentSerializer 

# Create your views here.
from rest_framework.generics import ListAPIView
# from django_filters.rest_framework import DjangoFilterBackend

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','passby','city']

    """def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby=user)"""

