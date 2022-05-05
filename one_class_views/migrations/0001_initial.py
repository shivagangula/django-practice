# Generated by Django 4.0.4 on 2022-05-01 15:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('department_name', models.CharField(max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Empolyee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('employee_name', models.CharField(max_length=25)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one_class_views.department')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]