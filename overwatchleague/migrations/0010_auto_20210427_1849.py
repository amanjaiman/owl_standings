# Generated by Django 3.2 on 2021-04-27 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overwatchleague', '0009_overwatchleague'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='cc_diff',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='diff',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='jj_diff',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='mm_diff',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='ss_diff',
            field=models.IntegerField(default=0),
        ),
    ]
