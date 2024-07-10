
# Generated by Django 5.0.7 on 2024-07-10 07:51

import django.db.models.deletion
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [

        ('user', '__first__'),

 
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('image_url', models.URLField(max_length=500)),

                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.user')),

            ],
        ),
    ]
