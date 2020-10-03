from django.db import models
from django_enumfield import enum
from django.db.models import CheckConstraint, Q, F
from enumchoicefield import ChoiceEnum, EnumChoiceField

# Create your models here.


class Employee(models.Model):
    EMPLOYEE_TYPES = (
        (0,  ('WAITER')),
        (1, ('COOK')),
        (2, ('ADMIN')),
    )
    id = models.AutoField(primary_key=True)
    employeeType = models.PositiveSmallIntegerField(
        choices=EMPLOYEE_TYPES, default=0)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=80, unique=True)
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Table(models.Model):
    id = models.AutoField(primary_key=True)
    inactive = models.BooleanField(default=False)


class MenuItem(models.Model):
    CATEGORIES = (
        (0,  ('STARTER')),
        (1, ('MAIN_COURSE')),
        (2, ('DESSERT')),
        (3, ('BEVERAGE')),
        (4, ('CAFETERIA'))
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    category = models.PositiveSmallIntegerField(choices=CATEGORIES, default=0)
    subCategory = models.CharField(max_length=100)
    unitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    menuItem = models.ManyToManyField(MenuItem, blank=True)
    quantity = models.IntegerField()
    comments = models.CharField(max_length=100)
    cancelled = models.BooleanField(default=True)


class State(enum.Enum):
    IN_PROCESS = 0
    CLOSED = 1
    CANCELLED = 2
    DELIVERED = 3


class Session(models.Model):
    id = models.AutoField(primary_key=True)
    waiter = models.ForeignKey(Employee, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order, blank=False)
    checkPlease = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    closeDate = models.DateTimeField(auto_now_add=True)
    state = enum.EnumField(State, default=State.IN_PROCESS)
