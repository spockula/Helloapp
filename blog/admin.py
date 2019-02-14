from webbrowser import register

from django.contrib import admin

from blog.models import PostType, Post,Author

# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(PostType)
