# Generated by Django 3.1.4 on 2021-01-15 11:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('type', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('number_of_seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_owner', models.CharField(max_length=120)),
                ('name_owner', models.CharField(max_length=120)),
                ('full_name', models.CharField(max_length=120)),
                ('contact_number', models.CharField(max_length=120)),
                ('opening_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=120)),
                ('position', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Popularity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('number_of_visitors', models.IntegerField()),
                ('object_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.object')),
            ],
        ),
        migrations.AddField(
            model_name='object',
            name='owner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.owner'),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_event', models.DateField(default=datetime.date.today)),
                ('type_of_event', models.CharField(max_length=120)),
                ('object_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.object')),
            ],
        ),
    ]
