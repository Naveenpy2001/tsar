# Generated by Django 4.2.6 on 2024-04-05 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_mediapost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediapost',
            name='image1',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='mediapost',
            name='image2',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
