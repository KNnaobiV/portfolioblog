from django.contrib import admin
from website.models import Post, Comment, Tag
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'slug', 'published_status',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'body')
    ordering = ('published_status', 'published')
    list_filter = ('title', 'body', 'tag')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post')
    ordering = ('created',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name', 'post')
    list_display = ('name',)
    ordering = ('name',)
    #prepopulated_fields = {'slug': ('name',)}
