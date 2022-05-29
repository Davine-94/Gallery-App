# Generated by Django 4.0.4 on 2022-05-29 15:04

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='media.category')),
                ('location', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='media.location')),
            ],
        ),
    ]