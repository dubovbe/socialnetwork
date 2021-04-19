from django.contrib import admin

from core.models import User, Post, Group

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Group)
