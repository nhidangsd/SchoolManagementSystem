# Generated by Django 3.1.1 on 2020-10-07 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_auto_20201006_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='seats_occupied',
        ),
    ]