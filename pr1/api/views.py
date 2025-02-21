from django.shortcuts import render
import io 
from api.serializer import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from api.models import Student
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator

# Create your views here.

# @csrf_exempt
@method_decorator(csrf_exempt, name='dispatch')
# def students(request):
class StudentAPI(View): 
    # if request.method == 'GET':
    def get(self, request, *args, **kwargs):
        if request.body:
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id', None) 
        
        if id: 
            modelobject = Student.objects.filter(id=id)
        else: 
            modelobject = Student.objects.all()
        

        if not modelobject.exists():
            data = {'msg': 'Data Not Found'}
            json_data = json.dumps(data)
            return HttpResponse(json_data, content_type='application/json')
        
        serialized_data = StudentSerializer(modelobject, many=True)
        
        json_data = JSONRenderer().render(serialized_data.data)
        return HttpResponse(json_data, content_type='application/json')     

    def post(self, request, *args, **kwargs):
    # if request.method == 'POST':
        if request.body:
            json_data = request.body 
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            serialized_data = StudentSerializer(data = python_data)
            if serialized_data.is_valid():
                print('validated_data ============', serialized_data.validated_data)
                serialized_data.save()
                response = {'msg': 'The data inserted successfully'}
                json_data = JSONRenderer().render(response)
                return HttpResponse(json_data, content_type='application/json')
            
            error_data = JSONRenderer().render(serialized_data.errors)
            return HttpResponse(error_data, content_type = 'application/json') 
        
    def put(self, request, *args, **kwargs):
    # if request.method == 'PUT':
        if request.body:
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id', None)
            if id:
                modelobject = Student.objects.get(id=id)
                serialized_data = StudentSerializer(modelobject, data=python_data, partial=True)
                if serialized_data.is_valid():
                    serialized_data.save()
                    response = {'msg': 'Data updated Successfully'}
                    return JsonResponse(response, safe=True)
                return JsonResponse(serialized_data.errors, safe=False)
            else:
                response = {'msg': 'Provide id'}
                return JsonResponse(response, safe=True)


    def delete(self, request, *args, **kwargs):
    # if request.method == 'DELETE':
        if request.body:
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id', None)
            if id:
                modelobject = Student.objects.get(id=id).delete()
                response = {'msg': 'Data deleted Successfully'}
                return JsonResponse(response, safe=True)
            else:
                response = {'msg': 'Provide id'}
                return JsonResponse(response, safe=True)

    

    

            
            


