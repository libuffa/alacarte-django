from rest_framework import serializers
from .models import Employee, EmployeeType
from django_enumfield import enum
from enumchoicefield import ChoiceEnum, EnumChoiceField

class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    # employeeType = serializers.ChoiceField(choices=[
    #         "WAITER"
    #     ]) 
    name = serializers.CharField(required=True, max_length=50)
    lastname = serializers.CharField(required=True, max_length=50)
    email = serializers.EmailField(required=True, max_length=80)
    user = serializers.CharField(required=True, max_length=50)
    password = serializers.CharField(required=True, max_length=50)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

"""
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from alacartebackend.models import Employee, EmployeeType
from alacartebackend.serializers import EmployeeSerializer
employee=Employee(1,"lautaro","buffa","lbuffa@gmail.com","lbuffa","1234")
serializer=EmployeeSerializer(employee)
serializer.data
content = JSONRenderer().render(serializer.data)
content
import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)
serializer = EmployeeSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()
# <Snippet: Snippet object>
"""
