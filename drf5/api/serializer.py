from rest_framework import serializers
from api.models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=200)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)

        instance.save()
        return instance

    def validate_roll(self, value):
        print('validate kar raha haii? ')
        if value > 200:
            raise serializers.ValidationError('Seats Full')
        return value

    # if validate_roll() cause no issues then validate will be called.
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        if name == 'Amit' and city != 'Mumbai':
            raise serializers.ValidationError('Enter correct city')
        return data

    