from django.contrib import admin
from django.db import models
from .models import Blog, Tag, Comment, Menu
from django.forms import Textarea
from mptt.admin import MPTTModelAdmin
from .models import Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_active')
    search_fields = ('title', 'description')

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'cols': 80, 'rows': 30})},
    }
    fields = ('title', 'main_image', 'description', 'author', 'category', 'tags', 'is_active')  # Ensure description is here

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Menu)


class CategoryAdmin(MPTTModelAdmin):
    list_display = ('title', 'parent')
    change_list_template = 'admin/change_list.html'  # Use the default Django admin template

admin.site.register(Category, CategoryAdmin)
