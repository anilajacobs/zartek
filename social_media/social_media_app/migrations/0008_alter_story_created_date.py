# Generated by Django 3.2.5 on 2021-07-05 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_media_app', '0007_rename_story_storystatus_story_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
