from django.contrib import admin
from .models import Post, Comments
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

@admin.register(Comments)
class CommmentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')