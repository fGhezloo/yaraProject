# Generated by Django 2.1.7 on 2019-03-05 20:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('dateTime', models.DateTimeField()),
                ('purchase', models.CharField(max_length=150)),
                ('purchaseID', models.IntegerField(primary_key=True, serialize=False)),
                ('userID', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('phoneNumber', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '09999999999' or '+989999999999'.", regex='^(\\+98|0)?9\\d{9}$')])),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
    ]
