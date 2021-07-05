
from rest_framework import serializers
from social_media_app.models import Story, StoryStatus, Weightage

class StorySerialzer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = ('name', 'description', 'tag', 'weight', 'upload',)

    def create(self, validated_data, user_id):
        validated_data['user_id'] = user_id
        tags = validated_data.pop("tag", [])
        image = validated_data.pop("upload", '')
        story_obj = Story.objects.create(**validated_data, upload=image)
        for i in tags:
            story_obj.tag.add(i)

class StoryListSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = "__all__"

class StoryStatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StoryStatus
        fields = "__all__"

statuses =( 
    ('like', 'Like'),
    ('dislike', 'Dislike'),
)
  
class StoryCardResponseSerialzer(serializers.Serializer):
    status = serializers.ChoiceField(choices = statuses)
    
    def create(self, validated_data, instance, user):
        validated_data['user'] = user
        validated_data['story_id'] = instance
        obj_data = instance.tag.all()
        story_weightage = instance.weight
        status = validated_data.pop("status")
        for i in obj_data:
            story_data, _ = Weightage.objects.get_or_create(user=user, tag=i)
        if status == 'like':
            story_data.weight = story_data.weight + story_weightage
        else:
            story_data.weight = story_data.weight - story_weightage
        story_data.save()