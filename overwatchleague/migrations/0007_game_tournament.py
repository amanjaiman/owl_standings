# Generated by Django 3.2 on 2021-04-27 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overwatchleague', '0006_overwatchleague'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='tournament',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
