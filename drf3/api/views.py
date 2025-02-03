from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from api.models import Student
from api.serializer import StudentSerializer
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def get_students(request):
    if request.method == 'GET': 
        if request.body: 
            json_data = request.body 
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id', None)
        else: 
            id = None 

        modelobject = Student.objects.filter(id=id) if id else Student.objects.all() 

        if not modelobject.exists():
            response = {'msg': 'No Student Found'}
            response = json.dumps(response)
            return HttpResponse(response, content_type='application/json')

        serialized_data = StudentSerializer(modelobject, many=True)
        json_data = JSONRenderer().render(serialized_data.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        if request.body:
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            serialized_data = StudentSerializer(data=python_data)
            if serialized_data.is_valid():
                serialized_data.save()
                response = {'msg':'Data inserted successfully'}
                # json_data = json.dumps(response)
                json_data = JSONRenderer().render(response)
                return HttpResponse(json_data, content_type = 'application/json')
            
            error_data = JSONRenderer().render(serialized_data.errors)
            return HttpResponse(error_data, content_type='application/json')

    
    if request.method == 'PUT':
        if request.body:
            json_data = request.body 
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id', None)
            original_data = Student.objects.filter(id=id).first()
            serialized_data = StudentSerializer(original_data, data=python_data, partial=True)
            # if complete data to be update
            # serialized_data = StudentSerializer(original_data, data=python_data)s
            if serialized_data.is_valid():
                serialized_data.save()
                response = {'msg': 'Data Updated Successfully'}
                json_data = JSONRenderer().render(response)
                return HttpResponse(json_data, content_type = 'application/json')
            json_data = JSONRenderer().render(serialized_data.errors)
            return HttpResponse(json_data, content_type = 'application/json')





            
                

