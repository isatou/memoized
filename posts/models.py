from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
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
    added_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    is_flagged = models.BooleanField(default=False)
    category = models.IntegerField(choices=POST_CATEGORIES, null=False, blank=False)

    def __unicode__(self):
        return self.title


class Upvote(models.Model):
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s - %s' % (self.voted_by.user.id, self.post.id)


class Downvote(models.Model):
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s - %s' % (self.voted_by.user.id, self.post.id)


class PinnedPost(models.Model):
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    pinned_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s - %s' % (self.pinned_by.user.id, self.post.id)


class Tag(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)

    def __unicode__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False, unique=True)
    description = models.TextField()
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False) # is_featured?

    def __unicode__(self):
        return self.name