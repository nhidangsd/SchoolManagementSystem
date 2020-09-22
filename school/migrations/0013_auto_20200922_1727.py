# Generated by Django 3.1.1 on 2020-09-22 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_auto_20200919_0142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='date_time_held',
            new_name='time',
        ),
        migrations.AddField(
            model_name='course',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
