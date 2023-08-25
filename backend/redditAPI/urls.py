from django.contrib import admin
from django.urls import path
from .views import RedditAPIView

urlpatterns = [
    path('reddit/view/<str:sub>', RedditAPIView.as_view(), name='reddit_view'),
]