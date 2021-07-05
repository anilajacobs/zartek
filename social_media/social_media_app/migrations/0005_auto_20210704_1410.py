# Generated by Django 3.2.5 on 2021-07-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_media_app', '0004_storyimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='upload',
            field=models.ImageField(blank=True, null=True, upload_to='media/story-images'),
        ),
        migrations.DeleteModel(
            name='StoryImage',
        ),
    ]
