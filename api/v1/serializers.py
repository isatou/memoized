from rest_framework import serializers

from posts.models import (
    Post, Upvote, Downvote, PinnedPost,
    Tag, Collection)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = '__all__'


class DownvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Downvote
        fields = '__all__'


class PinnedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PinnedPost
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'