# Generated by Django 5.0 on 2024-01-11 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('patient_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('health_issue', models.CharField(max_length=20)),
                ('doctor_name', models.CharField(max_length=20)),
                ('my_files', models.FileField(upload_to='Healthify')),
                ('comments', models.TextField()),
            ],
        ),
    ]