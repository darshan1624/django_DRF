from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from api.models import Student
from api.serializer import StudentSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def studentApi(request):
    print(request.method)
    if request.method == 'GET':
        id = None
        if request.body:
            stream = io.BytesIO(request.body)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id', None)
            if id:
                student_query = Student.objects.filter(id=id)[0]
                print(student_query)
                serialized_data = StudentSerializer(student_query)
        
        if not id:
            student_query = Student.objects.all()
            serialized_data = StudentSerializer(student_query, many=True)
        
        json_data = JSONRenderer().render(serialized_data.data)

        return HttpResponse(json_data, content_type = 'application/json')

    
    if request.method == 'POST':
        print('inside_post')
        if request.body:
            stream = io.BytesIO(request.body)
            print(request.body)
            python_data = JSONParser().parse(stream)
            serialized_data = StudentSerializer(data = python_data)
            if serialized_data.is_valid():
                print('======================',serialized_data.validated_data)
                serialized_data.save()
                response = {'msg': 'Data created Successfully'}
                return JsonResponse(response)
            return JsonResponse(serialized_data.errors)

    if request.method == 'PUT':
        if request.body:
            stream = io.BytesIO(request.body)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id', None)
            if id:
                model_object = Student.objects.filter(id=id)[0]
                serialized_data = StudentSerializer(model_object, data=python_data)
                if serialized_data.is_valid():
                    serialized_data.save()
                    response = {'msg': 'Data updated Successfully'}
                    return JsonResponse(response)
                return JsonResponse(serialized_data.errors)

    if request.method == 'DELETE':
        if request.body:
            stream = io.BytesIO(request.body)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id', None)
            if id:
                model_object = Student.objects.filter(id=id)[0]
                if model_object:
                    model_object.delete()
                    response = {'msg': 'Data deleted Successfully'}
                    return JsonResponse(response)
                
            response = {'msg': 'Invalid id'}
            return JsonResponse(response)
        
                    



        




        