from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from api.models import Student
from api.serializer import StudentSerializer
from django.http import HttpResponse
import json

# Create your views here.

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


            
                

