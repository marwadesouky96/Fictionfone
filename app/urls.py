from django.urls import path
from django.conf.urls import url
from rest_framework import routers
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'tweets/', views.TweetListAPIView.as_view(), name='tweet-list'),
    # path('tweets/',views.tweets, name='tweets'),
    # path('show_tweets/',views.show_tweets, name='show_tweets'),   
]