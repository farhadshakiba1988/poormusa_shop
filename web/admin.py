from django.contrib import admin

from web.models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'description']


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ['title', 'category', 'created_at']


admin.site.register(Article, ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'cover']


admin.site.register(Category, CategoryAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'description']


admin.site.register(UserProfile, UserProfileAdmin)
