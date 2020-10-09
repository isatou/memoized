from rest_framework import viewsets
from posts.models import (
    Post, Upvote, Downvote, PinnedPost,
    Tag, Collection, UpvoteCollection, DownvoteCollection)

from api.v1.serializers import (
    PostSerializer, UpvoteSerializer, DownvoteSerializer,
    PinnedPostSerializer, TagSerializer, CollectionSerializer,
    DownvoteCollectionSerializer, UpvoteCollectionSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(is_flagged=False)


class UpvoteViewSet(viewsets.ModelViewSet):
    serializer_class = UpvoteSerializer

    def get_queryset(self):
        return Upvote.objects.all()


class DownvoteViewSet(viewsets.ModelViewSet):
    serializer_class = DownvoteSerializer

    def get_queryset(self):
        return Downvote.objects.all()


class PinnedPostViewSet(viewsets.ModelViewSet):
    serializer_class = PinnedPostSerializer

    def get_queryset(self):
        return PinnedPost.objects.all()


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.all()


class CollectionViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionSerializer

    def get_queryset(self):
        return Collection.objects.all()


class UpvoteCollectionViewSet(viewsets.ModelViewSet):
    serializer_class = UpvoteCollectionSerializer

    def get_queryset(self):
        return UpvoteCollection.objects.all()


class DownvoteCollectionViewSet(viewsets.ModelViewSet):
    serializer_class = DownvoteCollectionSerializer

    def get_queryset(self):
        return DownvoteCollection.objects.all()
