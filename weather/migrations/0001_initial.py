# Generated by Django 4.0.2 on 2022-04-12 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('metrics', models.CharField(choices=[('Fahrenheit', 'Fahrenheit'), ('Celsius', 'Celsius'), ('Kelvin', 'Kelvin')], max_length=100)),
            ],
        ),
    ]