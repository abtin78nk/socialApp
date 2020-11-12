from django.urls import path
from .views import (home_view,
                    tweet_detail_view,
                    tweet_list_view,
                    tweet_create_view)

app_name = 'Tweets'
urlpatterns = [
    path('',home_view,name='Tweet-home'),
    path('tweets/',tweet_list_view, name='tweet-list'),
    path('tweets/<int:tweet_id>/',tweet_detail_view, name='tweet-detail'),
    path('create-tweet',tweet_create_view,name='tweetCreation')
]