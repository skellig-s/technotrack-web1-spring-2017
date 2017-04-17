# This Python file uses the following encoding: utf-8

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from posts.models import Blog, Post, Category, PostLike
from comments.models import Comment


class UserAdmin(BaseUserAdmin):

    fieldsets = BaseUserAdmin.fieldsets + (
        (u'Дополнительно', {'fields': ('admin_avatar', 'avatar')}),
    )
    readonly_fields = ('admin_avatar',)

    def admin_avatar(self, instance):
        return instance.avatar and u'<img src="{0}" width="100px" />'.format(
            instance.avatar.url
        )
    admin_avatar.allow_tags = True
    admin_avatar.short_description = u'Аватар'


admin.site.register(User, UserAdmin)
admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(PostLike)