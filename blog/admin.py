from django.contrib import admin
from .models import Category, Post

admin.site.site_header = 'Portfolio Admin'
admin.site.site_title = 'Portfolio Admin Area'
admin.site.index_title = 'Welcome to the Portfolio Admin Area'


class CategoryAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)