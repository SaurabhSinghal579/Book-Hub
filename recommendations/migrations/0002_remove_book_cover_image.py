# Generated by Django 5.0.7 on 2024-08-15 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover_image',
        ),
    ]
