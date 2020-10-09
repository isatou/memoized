from django.contrib import admin
from posts.models import (
    Post, Upvote, Downvote, PinnedPost,
    Tag, Collection)

# Register your models here.


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