# Generated by Django 2.0.1 on 2018-01-21 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restexample', '0006_auto_20180121_0920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='name',
        ),
    ]
