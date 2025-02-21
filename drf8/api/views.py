from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view(['GET'])
# def studentapi(request):

@api_view(['GET','POST'])
def studentapi(request):
    if request.method == 'GET':
        data = {'msg':'Get the data'}
        return Response(data)

    if request.method == 'POST':
        print(request.data)
        data = {'msg':'POST request'}
        return Response(data)






