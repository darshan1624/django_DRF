from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from api.serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)

        serialized_data =  StudentSerializer(data=python_data)
        if serialized_data.is_valid():
            serialized_data.save()

            response = {'msg':'Data Created'}
            json_data = JSONRenderer().render(response)   # this returns data in bytes 
            # json_data = json.dumps(response)   # this returns json data in string format 
            return HttpResponse(json_data, content_type='application/json')

        print('t1==',serialized_data.errors)
        error_data = JSONRenderer().render(serialized_data.errors)
        print('t2==',error_data)
        return HttpResponse(error_data, content_type='application/json')
