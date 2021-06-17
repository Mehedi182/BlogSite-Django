from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'intro', 'user')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'user')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
