# Generated by Django 4.2.6 on 2024-04-04 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image1', models.ImageField(upload_to='uploads/')),
                ('image2', models.ImageField(upload_to='uploads/')),
                ('narration', models.TextField()),
            ],
        ),
    ]
