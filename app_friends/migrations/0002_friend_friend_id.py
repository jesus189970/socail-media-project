# Generated by Django 2.2 on 2020-11-13 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_friends', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='friend_id',
            field=models.IntegerField(null=True),
        ),
    ]
