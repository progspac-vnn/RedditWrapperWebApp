from rest_framework import serializers

class RedditSerializer(serializers.Serializer):
        title = serializers.CharField()
        author = serializers.CharField()
        content = serializers.CharField(allow_blank = True)
        created_at = serializers.DateTimeField()
        image_url = serializers.URLField(allow_blank = True)
        video_url = serializers.URLField(allow_blank = True)
        post_url = serializers.URLField(allow_blank = True)