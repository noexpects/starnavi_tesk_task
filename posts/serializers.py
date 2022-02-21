from django.utils import timezone
from rest_framework import serializers

from .models import Post, Upvote


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ("id", "title", "author", "content", "creation_date", 'upvotes')


class AnaliticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = '__all__'


class DateRangeSerializer(serializers.Serializer):
    date_from = serializers.DateField()
    date_to = serializers.DateField(default=timezone.now().strftime("%Y-%m-%d"))
