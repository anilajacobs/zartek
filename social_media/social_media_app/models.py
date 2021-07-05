from django.db import models
from django.contrib.auth.models import User

class Tags(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Story(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    tag = models.ManyToManyField(Tags)
    weight = models.IntegerField(default=0) 
    created_date=models.DateField(auto_now_add=True)
    upload = models.ImageField(upload_to="media/story-images", null=True, blank=True)

    class Meta:
        ordering = ['weight']

class StoryStatus(models.Model):
    STORY_STATUS = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    )
    story_id = models.ForeignKey(Story, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STORY_STATUS)

class Weightage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)

    def get_full_name(self):
        return self.user.first_name
   