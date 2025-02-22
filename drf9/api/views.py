from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from api.serializer import StudentSerilaizer
from api.models import Student

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def studentapi(request, id=None):
    if request.method == 'GET':
        # id = request.data.get('id')
        if id:
            stuModelObject = Student.objects.get(id=id)
            serilaized_data = StudentSerilaizer(stuModelObject)
            return Response(serilaized_data.data)
        stuQueryObject = Student.objects.all()
        serilaized_data = StudentSerilaizer(stuQueryObject  , many=True)
        return Response(serilaized_data.data)
        
    if request.method == 'POST':
        serilaized_data = StudentSerilaizer(data = request.data)
        if serilaized_data.is_valid():
            serilaized_data.save()
            context = {'msg': 'Data created'}
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serilaized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        # id = request.data.get('id')
        if id:
            stuModelObject = Student.objects.get(id=id)
            serilaized_data = StudentSerilaizer(stuModelObject, data=request.data)
            if serilaized_data.is_valid():
                serilaized_data.save()
                context = {'msg': 'Data Updated Successfully'}
                return Response(context)
            return Response(serilaized_data.errors)

    if request.method == 'PATCH':
        # id = request.data.get('id')
        if id:
            stuModelObject = Student.objects.get(id=id)
            serilaized_data = StudentSerilaizer(stuModelObject, data=request.data, partial=True)
            if serilaized_data.is_valid():
                serilaized_data.save()
                context = {'msg': 'Data Updated Successfully'}
                return Response(context)
            return Response(serilaized_data.errors)
            
    if request.method == 'DELETE':
        # id = request.data.get('id')
        if id:
            Student.objects.get(id=id).delete()
            context = {'msg': 'Data Deleted Successfully'}
            return Response(context)
