# Generated by Django 4.2.6 on 2024-04-10 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_userregistration_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='resume',
            field=models.FileField(upload_to='resumes/'),
        ),
    ]