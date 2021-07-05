from rest_framework import generics
from social_media_app.serializers import StorySerialzer, StoryListSerialzer, StoryStatusSerializer, StoryCardResponseSerialzer
from rest_framework.response import Response
from social_media_app.models import Story,StoryStatus
from django.contrib.auth.models import User
from .pagination import LargeResultsSetPagination

class StoryCreateAPIView(generics.CreateAPIView):
   
    serializer_class = StorySerialzer
    pagination_class = LargeResultsSetPagination
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            users=request.user
            serializer.create(validated_data=serializer.validated_data,user_id=users)
            return Response("Success")
        else:
            return Response("Fail")

class StoryAPIView(generics.ListAPIView):

    serializer_class = StoryListSerialzer
    pagination_class = LargeResultsSetPagination
    def get_queryset(self):
        return Story.objects.all().order_by('-weight')

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response("Success")


class StoryStatusCountAPIView(generics.GenericAPIView):

    pagination_class = LargeResultsSetPagination
    def get(self, request, id):
        status_count = self.request.POST.copy()
        data_list = StoryStatus.objects.filter(story_id=id)
        status_count["liked_count"] = data_list.filter(status="like").count()
        status_count["disliked_count"] = data_list.filter(status="dislike").count()
        return_dict = {'response':status_count}
        return Response(return_dict)  

class StoryListAPIView(generics.ListAPIView):
    
    pagination_class = LargeResultsSetPagination
    def get(self,*args, **kwargs): 
        value=[]
        obj = Story.objects.order_by('-weight')
        for i in obj:
            data={}
            story_obj=Story.objects.filter(id=i.id)
            serializer=StorySerialzer(story_obj,many=True)
            data["name"]=serializer.data[0]['name'] 
            data["description"]=serializer.data[0]['description'] 
            data["upload"]=serializer.data[0]['upload'] 
            data["created_date"] = i.created_date
            storystatus_obj=StoryStatus.objects.filter(story_id=i.id)
            data["liked_count"] = storystatus_obj.filter(status="like").count() 
            data["disliked_count"] = storystatus_obj.filter(status="dislike").count()
            serializers=StoryStatusSerializer(storystatus_obj,many=True)
            data["status"]=serializers.data 
            value.append(data)
        return Response({"response":value})

class StoryLikeDislikeAPIView(generics.CreateAPIView):
    
    serializer_class = StoryCardResponseSerialzer
    pagination_class = LargeResultsSetPagination
    def get_queryset(self):
        try:
            return Story.objects.get(pk=self.kwargs.get('pk'))
        except:
            return None
    
    def post(self, request, *args, **kwargs):
        user_obj = User.objects.get(id=1)
        instance = self.get_queryset()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.create(validated_data=serializer.validated_data, instance=instance, user=user_obj)
            return Response("Success")
        else:
            return Response("Fail") 

class StoryUserAPIView(generics.ListAPIView):

    pagination_class = LargeResultsSetPagination
    def get(self,*args, **kwargs): 
        data = StoryStatus.objects.filter(story_id=self.kwargs.get('id')).filter(status="like") 
        value=[] 
        for i in data:
            name=i.user.username 
            value.append(name)
        return Response({"user_list":value})