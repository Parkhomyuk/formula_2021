# Generated by Django 3.1.2 on 2020-10-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula_app', '0002_remove_position_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolyear',
            name='year',
            field=models.CharField(max_length=10, null=True),
        ),
    ]