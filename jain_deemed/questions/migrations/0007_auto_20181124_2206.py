# Generated by Django 2.1.3 on 2018-11-24 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20181124_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='day',
            field=models.DateTimeField(),
        ),
    ]
