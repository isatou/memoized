from django.contrib import admin
from posts.models import (
    Post, Upvote, Downvote, PinnedPost,
    Tag, Collection,
    DownvoteCollection, UpvoteCollection)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Upvote)
class UpvoteAdmin(admin.ModelAdmin):
    pass


@admin.register(Downvote)
class DownvoteAdmin(admin.ModelAdmin):
    pass


@admin.register(PinnedPost)
class PinnedPostAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass


@admin.register(UpvoteCollection)
class UpvoteCollectionAdmin(admin.ModelAdmin):
    pass


@admin.register(DownvoteCollection)
class DownvoteCollectionAdmin(admin.ModelAdmin):
    pass
