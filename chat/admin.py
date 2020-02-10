from django.contrib import admin 
from .models import Post, Comment

# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user','created_on')
    list_filter = ("user",)
    search_fields = ['title', 'content']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('body','user','create') 
    search_fields = ['user', 'body']

    
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)