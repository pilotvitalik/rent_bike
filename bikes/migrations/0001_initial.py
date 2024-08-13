# Generated by Django 5.1 on 2024-08-13 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('bike_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=100)),
                ('rent_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('photo', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
