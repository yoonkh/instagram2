from django.contrib import admin

from .models import Post, Comment, PostLike, User

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostLike)
admin.site.register(User)
