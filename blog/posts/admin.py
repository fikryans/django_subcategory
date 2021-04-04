from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from .models import Category, Post



class CategoryAdmin(DraggableMPTTAdmin):
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),

admin.site.register(Category,DraggableMPTTAdmin)


admin.site.register(Post)