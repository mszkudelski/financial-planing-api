# Generated by Django 2.0.1 on 2018-01-21 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restexample', '0005_plan_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
