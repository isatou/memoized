from django.db import models
from django.contrib.auth.models import User

from utils.model_mixins import BaseAppModelMixin


class Post(BaseAppModelMixin):
    HOW_TO = 0
    LESSONS_LEARNT = 1
    RESOURCES = 2
    POST_CATEGORIES = [
        (HOW_TO, 'How to'),
        (LESSONS_LEARNT, 'Lessons Learnt'),
        (RESOURCES, 'Resources'),
    ]

    title = models.CharField(max_length=75, blank=False, null=False)
    content = models.TextField()
    link = models.URLField(blank=True, null=True)
    added_by = models.ForeignKey(User, null=False, blank=False,
        on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    is_flagged = models.BooleanField(default=False)
    category = models.IntegerField(choices=POST_CATEGORIES, null=False,
    blank=False)
    tags = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Upvote(BaseAppModelMixin):
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)


    def __str__(self):
        return '%s - %s' % (self.voted_by.user.id, self.post.id)


class Downvote(BaseAppModelMixin):
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def __str_(self):
        return '%s - %s' % (self.voted_by.user.id, self.post.id)

class PinnedPost(BaseAppModelMixin):
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    pinned_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.pinned_by.user.id, self.post.id)


class Tag(BaseAppModelMixin):
    name = models.CharField(max_length=25, blank=False, null=False)

    def __str_(self):
        return self.name


class Collection(BaseAppModelMixin):
    name = models.CharField(max_length=25, blank=False, null=False, unique=True)
    description = models.TextField()
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=True)
    tags = models.TextField()

    def __str__(self):
        return self.name



class UpvoteCollection(BaseAppModelMixin):
    collection = models.ForeignKey(Collection, null=False, blank=False, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.voted_by.user.id, self.post.id)


class DownvoteCollection(BaseAppModelMixin):
    collection = models.ForeignKey(Collection, null=False, blank=False, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def __str_(self):
        return '%s - %s' % (self.voted_by.user.id, self.post.id)