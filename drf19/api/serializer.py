
from api.models import Student
from rest_framework import serializers

class StudentSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' 

    