# Generated by Django 3.2 on 2021-04-27 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overwatchleague', '0004_overwatchleague'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='week',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Week',
        ),
    ]
