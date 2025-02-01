from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.
from api.models import Student

def student_details(request, id):
    stu = Student.objects.get(pk=id)
    print(stu)
    serialized_data = StudentSerializer(stu)
    # json_data = JSONRenderer().render(serialized_data.data)
    # return HttpResponse(json_data, content_type='application/json')

    # Insteda of above 2 statements we can directly render serailazed data into json and return.
    # since serialized_data.data is in dict format. safe = True (by default safe is set to True)
    return JsonResponse(serialized_data.data)

def student_details_all(request):
    stu = Student.objects.all()
    print(stu)
    serialized_data = StudentSerializer(stu, many=True)
    print(serialized_data)
    print(serialized_data.data)
    # json_data = JSONRenderer().render(serialized_data.data)
    # print(json_data)

    # return HttpResponse(json_data, content_type='application/json')
    # To allow list of dicts also you need to set safe = False 
    return JsonResponse(serialized_data.data, safe=False)