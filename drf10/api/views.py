from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from api.models import Student
from api.serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status

class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        # id = request.data.get('id')
        if pk: 
            stuModelObject = Student.objects.get(id=pk)
            serialized_data = StudentSerializer(stuModelObject)
            return Response(serialized_data.data)
        stuQueryObject = Student.objects.all()
        serialized_data = StudentSerializer(stuQueryObject, many=True)
        return Response(serialized_data.data)

    def post(self, request, pk=None, format=None):
        python_data = request.data 
        print(python_data)
        serialized_data = StudentSerializer(data = python_data)
        if serialized_data.is_valid():
            serialized_data.save()
            context = {'msg': 'Data created'}
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None, format = None):
        # id = request.data.get('id')
        python_data = request.data
        if id: 
            stuModelObject = Student.objects.get(id=pk)
            serialized_data = StudentSerializer(stuModelObject,data=python_data, partial=True)
            if serialized_data.is_valid():
                serialized_data.save()
                context = {'msg': 'Data Updated'}
                return Response(context) 
            return Response(serialized_data.errors, status= status.HTTP_400_BAD_REQUEST)   

    def delete(self, request, pk=None, format = None):
        # id = request.data.get('id')
        Student.objects.get(id=pk).delete()
        context = {'msg': 'Data Deleted'}
        return Response(context)


