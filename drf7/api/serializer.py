from rest_framework import serializers
from api.models import Student

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)  #method 1
    class Meta:
        model = Student 
        fields = ['name', 'roll', 'city']
        # read_only = ['name']   #method 2
        extra_kwargs = {'name':{'read_only': True}}         #method 3

    