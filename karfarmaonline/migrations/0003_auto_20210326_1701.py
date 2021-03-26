# Generated by Django 3.1.7 on 2021-03-26 12:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('karfarmaonline', '0002_auto_20210326_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='title',
            field=models.CharField(max_length=200, verbose_name='عنوان هزینه کرد'),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='تاریخ ایجاد پروژه'),
        ),
    ]