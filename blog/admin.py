from django.contrib import admin

from blog.models import PostType, Post,Author

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('Last_Name', 'First_Name', 'Position')
    fields = ['First_Name', 'Last_Name', 'Position']

admin.site.register(Author, AuthorAdmin)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'Tags','pub_date', 'created_date', 'id')
    list_filter = ('title', 'Tags', 'pub_date')

@admin.register(PostType)
class PostTypeAdmin(admin.ModelAdmin):
    list_display = ('Post', 'id', 'Tag')

