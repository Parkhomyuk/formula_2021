# Generated by Django 3.1.2 on 2020-10-22 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula_app', '0003_schoolyear_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='tour_name_suffics',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
