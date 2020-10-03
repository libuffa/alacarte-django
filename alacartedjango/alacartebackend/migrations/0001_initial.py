# Generated by Django 2.2.16 on 2020-10-03 02:19

import alacartebackend.models
from django.db import migrations, models
import django.db.models.deletion
import django_enumfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=80, unique=True)),
                ('user', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('category', django_enumfield.db.fields.EnumField(enum=alacartebackend.models.Category)),
                ('subCategory', models.CharField(max_length=100)),
                ('unitPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('comments', models.CharField(max_length=100)),
                ('cancelled', models.BooleanField(default=True)),
                ('menuItem', models.ManyToManyField(blank=True, to='alacartebackend.MenuItem')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('inactive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('checkPlease', models.BooleanField(default=False)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('closeDate', models.DateTimeField(auto_now_add=True)),
                ('state', django_enumfield.db.fields.EnumField(default=0, enum=alacartebackend.models.State)),
                ('orders', models.ManyToManyField(to='alacartebackend.Order')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alacartebackend.Table')),
                ('waiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alacartebackend.Employee')),
            ],
        ),
    ]
