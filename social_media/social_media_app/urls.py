
from django.urls import path
from social_media_app import views
from rest_framework_swagger.views import get_swagger_view

# schema_view = get_swagger_view(title='SOCIAL MEDIA')
urlpatterns = [
    # path('', schema_view),

    # Admin
    path('create-story/', views.StoryCreateAPIView.as_view(), name='create-story'),  
    path('story/', views.StoryAPIView.as_view(), name='story'),  
    path('story-status-count/<int:id>/', views.StoryStatusCountAPIView.as_view(), name='story-status-count'), 

    # # User
    path('story-list/', views.StoryListAPIView.as_view(), name='story-list'), 
    path('story-like-dislike/<int:pk>/', views.StoryLikeDislikeAPIView.as_view(), name='story-like-dislike'),  
    path('story-user-liked/<int:id>/', views.StoryUserAPIView.as_view(), name='story-user-liked'), 
]