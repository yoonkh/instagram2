from django.contrib.auth import get_user_model
from django.db import models

from module.timemixin import TimeMixinStamp

User = get_user_model()


class Post(TimeMixinStamp):
    author = models.ForeignKey(User)
    photo = models.ImageField(upload_to='post%y%m%d', blank=True)
    like_users = models.ManyToManyField(
        User,
        through='PostLike',
        related_name='like_users',
    )


class Comment(TimeMixinStamp):
    author = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    content = models.TextField()


class PostLike(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)