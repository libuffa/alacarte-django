from django.db import models

# Create your models here.


class Waiter(models.Model):
    # id = models.IntegerField()
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Table(models.Model):
    # id = models.IntegerField()
    inactive = models.BooleanField()


class Order(models.Model):
    # id = models.IntegerField()
    quantity = models.IntegerField()
    comments = models.CharField(max_length=100)
    cancelled = models.BooleanField()


# class Session(models.Model):
    # id = models.IntegerField()
