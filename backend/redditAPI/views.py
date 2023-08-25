from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from .serializers import RedditSerializer
import praw
from django.conf import settings
import re

class RedditAPIView(APIView):
    def get(self, request, sub):
        try:
            subreddit_name = sub
            print("Subreddit Name:", subreddit_name)

            # Check if data is cached
            cached_data = cache.get(f'reddit_{sub}')
            if cached_data:
                return Response(cached_data, status=status.HTTP_200_OK)

            # API credentials
            reddit = praw.Reddit(
                client_id=settings.REDDIT_CLIENT_ID,
                client_secret=settings.REDDIT_CLIENT_SECRET,
                username='USERNAME',
                password='PASSWORD',
                user_agent='test-api',
            )

            # Fetch 10 data from Reddit
            subreddit = reddit.subreddit(subreddit_name) if subreddit_name else reddit.subreddit('movies')
            hot_posts = subreddit.hot(limit=10)

            # Process and serialize the data
            serialized_posts = []

            for post in hot_posts:
                post_data = {
                    'title': post.title,
                    'author': post.author.name,
                    'created_at': datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
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

            # Cache the data for 15 minutes
            cache.set(f'reddit_{sub}', serializer.data, 60 * 15)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
