# Generated by Django 3.2 on 2021-04-29 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overwatchleague', '0013_auto_20210428_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='region',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]
