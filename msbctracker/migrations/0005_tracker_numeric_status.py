# Generated by Django 4.1 on 2022-10-08 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msbctracker', '0004_tracker_msbc_patch_api_call_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='numeric_status',
            field=models.CharField(default='', max_length=20),
        ),
    ]
