# Generated by Django 2.2.3 on 2019-08-09 18:10

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190805_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31, null=True),
        ),
    ]
