# Generated by Django 3.1.14 on 2024-05-04 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandy', '0008_auto_20240504_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='major_2',
            field=models.TextField(default='', max_length=60),
        ),
    ]
