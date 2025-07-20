from django.contrib import admin
from .models import News, Comment

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    fields = ('title', 'content', 'author', 'image')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'news', 'content', 'created_at', 'is_active')
    list_filter = ('created_at', 'is_active')
    search_fields = ('author__username', 'content')
    actions = ['activate_comments', 'deactivate_comments']

    def activate_comments(self, request, queryset):
        queryset.update(is_active=True)
    activate_comments.short_description = 'Активировать комментарии'

    def deactivate_comments(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_comments.short_description = 'Деактивировать комментарии'