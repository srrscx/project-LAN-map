# Generated by Django 5.0.3 on 2024-03-17 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_alter_devices_building_alter_devices_department_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices',
            name='status',
            field=models.CharField(default='unknown', max_length=10),
        ),
    ]
