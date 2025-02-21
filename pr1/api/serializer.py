from rest_framework import serializers
from api.models import Student

def start_with_r(value):
    if value[0].lower() == 'r':
        raise serializers.ValidationError('Name must not start with r.')
    return value

"""class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200, validators = [start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length = 200)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.roll = validate_data.get('roll', instance.roll)
        instance.city = validate_data.get('city', instance.city)

        instance.save()
        return instance """

class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length = 200, validators = [start_with_r])

    class Meta:
        model = Student
        fields = '__all__'
        exclude = []
    
    def validate_roll(self,value):
        if value > 200:
            raise serializers.ValidationError('Seats Full')
        return value

    def validate(self, data):
        name = data.get('name', None)
        city = data.get('city', None)
        if name.lower() == 'oliva' and city.lower() != 'mumbai':
            raise serializers.ValidationError('City must be mumbai.')
        return data 

