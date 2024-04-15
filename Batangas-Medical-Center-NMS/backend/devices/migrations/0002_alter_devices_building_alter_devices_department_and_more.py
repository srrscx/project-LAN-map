# Generated by Django 5.0.3 on 2024-03-17 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='building',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='devices',
            name='department',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='devices',
            name='deviceName',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='devices',
            name='deviceType',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='devices',
            name='floor',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]