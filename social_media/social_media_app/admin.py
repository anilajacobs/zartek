from django.contrib import admin
from .models import Tags,Story,StoryStatus,Weightage
# Register your models here.
admin.site.register(Tags),
admin.site.register(Story),
admin.site.register(StoryStatus),
admin.site.register(Weightage),