# Generated by Django 4.1.1 on 2022-09-21 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
