# Generated by Django 5.0.1 on 2024-07-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_beachcam_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='beachcam',
            name='url_youtube',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
