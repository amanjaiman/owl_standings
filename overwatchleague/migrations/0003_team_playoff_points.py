# Generated by Django 3.2 on 2021-04-27 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overwatchleague', '0002_overwatchleague'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='playoff_points',
            field=models.IntegerField(default=0),
        ),
    ]