# Generated by Django 4.1 on 2022-09-19 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_logs', models.JSONField(default='')),
                ('api_call_time', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='', max_length=20)),
                ('api_call_time', models.CharField(default='', max_length=10)),
                ('tracking_number', models.CharField(default='', max_length=20, unique=True)),
                ('updated_time', models.CharField(default='', max_length=10)),
                ('booked', models.CharField(default='', max_length=20)),
                ('arrival', models.CharField(default='', max_length=20)),
                ('delivered', models.CharField(default='', max_length=20)),
                ('outbound', models.CharField(default='', max_length=20)),
                ('tracking_info', models.JSONField(default='')),
            ],
        ),
    ]