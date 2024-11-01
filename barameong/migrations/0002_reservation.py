# Generated by Django 5.1.2 on 2024-10-31 12:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barameong', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('guest_name', models.CharField(default='guest', max_length=100)),
                ('reservation_number', models.CharField(max_length=8, unique=True)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barameong.dog')),
            ],
            options={
                'db_table': 'reservation',
            },
        ),
    ]
