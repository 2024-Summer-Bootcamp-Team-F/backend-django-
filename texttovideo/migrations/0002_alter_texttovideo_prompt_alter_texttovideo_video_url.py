# Generated by Django 5.0.6 on 2024-07-27 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texttovideo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texttovideo',
            name='prompt',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='texttovideo',
            name='video_url',
            field=models.CharField(max_length=2048),
        ),
    ]