from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    # employeeType = enum.EnumField(EmployeeType)
    name = serializers.CharField(required=True,max_length=50)
    lastname = serializers.CharField(required=True,max_length=50)
    email = serializers.EmailField(required=True, max_length=80)
    user = serializers.CharField(required=True,max_length=50)
    password = serializers.CharField(required=True,max_length=50)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)