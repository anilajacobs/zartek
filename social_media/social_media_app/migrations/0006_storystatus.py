# Generated by Django 3.2.5 on 2021-07-04 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social_media_app', '0005_auto_20210704_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('like', 'Like'), ('dislike', 'Dislike')], max_length=100)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_media_app.story')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
