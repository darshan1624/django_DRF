from django.shortcuts import render
from rest_framework.decorators import api_view
from api.serializer import StudentSerializer
from api.models import Student
from rest_framework.response import Response

# Create your views here.

@api_view(['GET', 'POST'])
def studentapi(request, id=None):
    if request.method == 'GET':
        python_data = request.data
        # id = python_data.get('id', None)
        if id:
            stu = Student.objects.filter(id=id)
            serialized_data = StudentSerializer(stu[0])
            return Response(serialized_data.data)
        else:
            stu = Student.objects.all()
            serialized_data = StudentSerializer(stu, many=True)
            print(serialized_data.data)
            return Response(serialized_data.data)
    
    if request.method == 'POST':
        python_data = request.data
        serialized_data = StudentSerializer(data = python_data)
        if serialized_data.is_valid():
            serialized_data.save()
            response = {'msg':'Record created'}
            return Response(response)
        return Response(serialized_data.errors)


