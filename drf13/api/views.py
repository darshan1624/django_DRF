from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from api.models import Student
from api.serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status

class StudentViewSet(viewsets.ViewSet):
    name = 'Students'       # Shown on browsable webpae 
    suffix = 'GetALLStudents'     # shown on browsable webapge      NAME-SUffix
    description = 'provides all students details'        # Just for documenting here
    def list(self, request):
        # self.suffix = 'GetALLStudents'
        # self.name = 'Students'
        print('basename', self.basename)
        print('action', self.action)
        print('detail', self.detail)
        print('suffix', self.suffix)
        print('name', self.name)
        print('description', self.description)
        stu = Student.objects.all()
        serialized_data = StudentSerializer(stu, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    
    def create(self,request):
        serialized_data = StudentSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            context = {'msg':"Data Created"}
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status= status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk = None):
        stu = Student.objects.get(id=pk)
        serialized_data =  StudentSerializer(stu)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        stu = Student.objects.get(id=pk)
        serialized_data =  StudentSerializer(stu, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            context = {'msg':"Data Updated"}
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status= status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        stu = Student.objects.get(id=pk)
        serialized_data =  StudentSerializer(stu, data=request.data, partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            context = {'msg':"Data Updated"}
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status= status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        stu = Student.objects.get(id=pk).delete()
        context = {'msg':"Data Deleted"}
        return Response(context, status=status.HTTP_204_NO_CONTENT)
        