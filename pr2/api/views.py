from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from api.models import Student
from api.serializer import StudentSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import View
from django.utils.decorators import method_decorator



# Create your views here.
# @csrf_exempt
# def studentApi(request):
#     if request.method == 'GET':
@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(View):
    def get(self, request, *args, **kwargs):
        id = None
        if request.body:
            stream = io.BytesIO(request.body)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id', None)
            if id:
                student_query = Student.objects.filter(id=id)
                if len(student_query) > 0:
                    serialized_data = StudentSerializer(student_query[0])
                else:
                    response = {'msg':'Invalid ID'}
                    # json_data = JSONRenderer().render(response)
                    return JsonResponse(response)
                    # return HttpResponse(json_data, content_type = 'application/json')
        
        if not id:
            student_query = Student.objects.all()
            serialized_data = StudentSerializer(student_query, many=True)
        
        json_data = JSONRenderer().render(serialized_data.data)

        return HttpResponse(json_data, content_type = 'application/json')

    
    # if request.method == 'POST':
    def post(self, request, *args, **kwargs):
        if request.body:
            stream = io.BytesIO(request.body)
            print(request.body)
            python_data = JSONParser().parse(stream)
            serialized_data = StudentSerializer(data = python_data)
            if serialized_data.is_valid():
                serialized_data.save()
                response = {'msg': 'Data created Successfully'}
                return JsonResponse(response)
            return JsonResponse(serialized_data.errors)

    # if request.method == 'PUT':
    def put(self, request, *args, **kwargs):
        if request.body:
            stream = io.BytesIO(request.body)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id', None)
            if id:
                model_object = Student.objects.filter(id=id)
                serialized_data = StudentSerializer(model_object[0], data=python_data)
                if serialized_data.is_valid():
                    serialized_data.save()
                    response = {'msg': 'Data updated Successfully'}
                    return JsonResponse(response)
                return JsonResponse(serialized_data.errors)

    # if request.method == 'DELETE':
    def delete(self,request, *args, **kwrags):
        if request.body:
            stream = io.BytesIO(request.body)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id', None)
            if id:
                model_object = Student.objects.filter(id=id)
                if model_object:
                    model_object[0].delete()
                    response = {'msg': 'Data deleted Successfully'}
                    return JsonResponse(response)
                
            response = {'msg': 'Invalid id'}
            return JsonResponse(response)
        
                    



        




        