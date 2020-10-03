from rest_framework import serializers
from .models import Employee, MenuItem
from django_enumfield import enum
from enumchoicefield import ChoiceEnum, EnumChoiceField


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    employeeType = serializers.IntegerField()
    name = serializers.CharField(required=True, max_length=50)
    lastname = serializers.CharField(required=True, max_length=50)
    email = serializers.EmailField(required=True, max_length=80)
    user = serializers.CharField(required=True, max_length=50)
    password = serializers.CharField(required=True, max_length=50)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.employeeType = validated_data.get('employeeType', instance.employeeType)
        instance.name = validated_data.get('name', instance.name)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.email = validated_data.get('email', instance.email)
        instance.unitPrice = validated_data.get('style', instance.unitPrice)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance


class MenuItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=50)
    description = serializers.CharField(required=True, max_length=100)
    category = serializers.IntegerField()
    subCategory = serializers.CharField(required=True, max_length=50)
    unitPrice = serializers.DecimalField(
        required=True, max_digits=10, decimal_places=2)
    active = serializers.BooleanField(required=True)

    def create(self, validated_data):
        return MenuItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.subCategory = validated_data.get('subCategory', instance.subCategory)
        instance.unitPrice = validated_data.get('unitPrice', instance.unitPrice)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance


"""
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from alacartebackend.models import Employee, EmployeeType, MenuItem
from alacartebackend.serializers import EmployeeSerializer, MenuItemSerializer

employee=Employee(1,"lautaro","buffa","lbuffa@gmail.com","lbuffa","1234")
menuItem=MenuItem(1,"milanesa","milanesa de lomo al horno",1,"minutas",100.00)

serializer=EmployeeSerializer(employee)
serializer.data
serializer=MenuItemSerializer(menuItem)
serializer.data
content = JSONRenderer().render(serializer.data)
content
import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)
data
serializer = MenuItemSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()
# <Snippet: Snippet object>
"""
