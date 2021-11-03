from django.contrib import admin

# Register your models here.
from .models import Post, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'content', 'date_created',)
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)

admin.site.site_header = 'PRIMUS DEI BLOG'
admin.site.site_title = 'Primus Admin Area'
admin.site.index_title = 'Welcome To Primus Admin Area'
