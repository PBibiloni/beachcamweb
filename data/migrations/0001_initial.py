# Generated by Django 5.0.1 on 2024-01-16 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeachCam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beach_name', models.CharField(max_length=200, unique=True)),
                ('beach_latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('beach_longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('url_image', models.CharField(max_length=200)),
                ('url_aemet', models.CharField(max_length=200, null=True)),
                ('url_platgesbalears', models.CharField(max_length=200, null=True)),
                ('probe_freq_mins', models.IntegerField(default=60)),
                ('max_crowd_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts', models.DateTimeField()),
                ('image', models.ImageField(null=True, upload_to='')),
                ('crowd_count', models.FloatField(default=0)),
                ('beachcam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.beachcam')),
            ],
        ),
    ]
