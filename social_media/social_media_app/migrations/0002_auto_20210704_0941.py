# Generated by Django 3.2.5 on 2021-07-04 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_media_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='story',
            name='last_updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
