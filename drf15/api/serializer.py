from rest_framework import serializers
from api.models import Student

class StudentSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

        