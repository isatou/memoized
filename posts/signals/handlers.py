from django.db.models.signals import post_save
from django.dispatch import receiver

from posts.models import (
    Upvote, Downvote,
    UpvoteCollection, DownvoteCollection
)


@receiver(post_save, sender=Upvote)
def save_upvote_post(sender, instance, **kwargs):
    """
    increate the upvote count
    """
    post = instance.post
    post.upvotes += 1
    post.save()


@receiver(post_save, sender=Downvote)
def save_downvote_post(sender, instance, **kwargs):
    """
    increate the downvote count
    """
    post = instance.post
    if post.downvotes > 1:
        post.downvotes -= 1
        post.save()


@receiver(post_save, sender=UpvoteCollection)
def save_upvote_collection(sender, instance, **kwargs):
    """
    increate the upvote collection
    """
    collection = instance.collection
    collection.upvotes += 1
    collection.save()


@receiver(post_save, sender=DownvoteCollection)
def save_downvote_collection(sender, instance, **kwargs):
    """
    increate the downvote collection
    """
    collection = instance.collection
    if collection.downvotes > 1:
        collection.downvotes -= 1
        collection.save()
