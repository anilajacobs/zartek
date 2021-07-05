How to run the project:
1. Install requirements using "pip install -r requirements.txt"
2. Run the url in localhost(like http://127.0.0.1:8000/)'



Url List:
1. http://127.0.0.1:8000/social_media/create-story/
2. http://127.0.0.1:8000/social_media/story-status-count/<int:id>/     # pass id as story id(story table id)
3. http://127.0.0.1:8000/social_media/story-list/
4. http://127.0.0.1:8000/social_media/story/
5. http://127.0.0.1:8000/social_media/story-like-dislike/<int:pk>/    # pk is the id of story
6. http://127.0.0.1:8000/social_media/story-user-liked/<int:id>/      # id is the id of story


superuser username: media
          password: media@123

**NB - Any authentication issue is occured then login superuser in adminpanel
