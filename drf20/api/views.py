from django.shortcuts import render
from api.models import Student
from api.serializer import StudentSerilaizer

# Create your views here.
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from api.customThrottling import CustomRateThrottle

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

"""class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerilaizer

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [CustomRateThrottle]
    """

class ListStudentApi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerilaizer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'list_retrive_api'

class CreateStudentApi(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerilaizer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'create_update_destroy_student_api'

class RetriveStudentApi(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerilaizer
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'list_retrive_api'


class UpdateStudentApi(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerilaizer
    # throttle_scope = 'create_update_destroy_student_api'


class DestroyStudentApi(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerilaizer
    throttle_scope = 'create_update_destroy_student_api'


