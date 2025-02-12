from rest_framework import serializers
from api.models import Student


def starts_with_r(value):
    if value[0] != 'r':
        raise serializers.ValidationError('Name must start with r')
    return value


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[starts_with_r])
    # name = serializers.CharField(read_only=True)  #method 1
    class Meta:
        model = Student 
        fields = ['name', 'roll', 'city']
        # read_only = ['name']   #method 2
        # extra_kwargs = {'name':{'read_only': True}}         #method 3



    def validate_roll(self, value):
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
