# Generated by Django 2.2.16 on 2020-10-02 20:23

import alacartebackend.models
from django.db import migrations, models
import django.db.models.deletion
import django_enumfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('alacartebackend', '0001_initial'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='order',
            name='cancelled',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='table',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='table',
            name='inactive',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='waiter',
            name='email',
            field=models.EmailField(max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='waiter',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
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
                ('waiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alacartebackend.Waiter')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='menuItem',
            field=models.ManyToManyField(blank=True, to='alacartebackend.MenuItem'),
        ),
    ]
