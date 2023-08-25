from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RedditSerializer
import praw
from django.conf import settings
import re

class RedditAPIView(APIView):
    def get(self, request):

        try:
            subreddit_name = request.GET.get('subreddit')
            print("Subreddit Name:", subreddit_name)
            # API credentials
            reddit = praw.Reddit(
                client_id = settings.REDDIT_CLIENT_ID,
                client_secret = settings.REDDIT_CLIENT_SECRET,
                username='USERNAME',
                password='PASSWORD',
                user_agent = 'test-api', # app name
            )

            # Fetch 10 data from reddit
            subreddit = reddit.subreddit(subreddit_name) if subreddit_name else reddit.subreddit('movies')
            hot_posts = subreddit.hot(limit=10)

            # Process and serialize the data 
            serialized_posts = []

            for post in hot_posts:
                post_data = {
                    'title': post.title,
                    'author': post.author.name,
                    'created_at': datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S'),  # Format the datetime
                    'content': post.selftext,
                    'image_url': post.url if post.url.endswith(('.png', '.jpg', '.jpeg', '.gif')) else None,
                    'video_url': None,
                    'post_url': f'https://www.reddit.com{post.permalink}' if post.permalink else None
                }

                if post.media and 'reddit_video' in post.media:
                    post_data['video_url'] = post.media['reddit_video']['fallback_url']

                serialized_posts.append(post_data)

            serializer = RedditSerializer(data=serialized_posts, many=True)
            serializer.is_valid()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error' : str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
