# Generated by Django 5.1 on 2025-03-01 08:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('father', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('pass1', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=10)),
                ('image', models.FileField(null=True, upload_to='uploads/users/')),
                ('address', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shoping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.CharField(max_length=20, null=True)),
                ('p_name', models.CharField(max_length=100)),
                ('p_quantity', models.IntegerField(null=True)),
                ('p_price', models.IntegerField()),
                ('p_image', models.FileField(null=True, upload_to='uploads/Shoping/')),
                ('p_date', models.DateTimeField(default=datetime.date(2025, 3, 1))),
            ],
        ),
    ]
