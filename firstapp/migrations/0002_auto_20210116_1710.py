# Generated by Django 3.1.4 on 2021-01-16 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backup_copy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='login',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
