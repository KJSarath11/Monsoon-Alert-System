# Generated by Django 5.1.4 on 2024-12-18 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FloodWarning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=100)),
                ('warning_level', models.CharField(max_length=100)),
                ('alert_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(max_length=100)),
                ('report_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
