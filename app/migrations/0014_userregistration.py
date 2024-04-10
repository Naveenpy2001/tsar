# Generated by Django 4.2.6 on 2024-04-10 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('country_code', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=100)),
                ('aadhar_card_number', models.CharField(max_length=20)),
                ('is_fresher', models.CharField(max_length=100)),
                ('applied_with_tsar_it', models.CharField(max_length=100)),
                ('previous_employee_id', models.CharField(max_length=50)),
                ('receive_job_notifications', models.BooleanField(default=False)),
                ('hear_about_opportunities', models.BooleanField(default=False)),
                ('terms_of_use_agreed', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
