from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display=["title",  "is_active", "is_new", "is_contest", "is_event", "created_at", "slug"]
    list_editable=["is_active", "is_new", "is_event", "is_contest"]
    search_fields=["title", "content"]
    readonly_fields=["slug"]
    list_filter=["created_at"]
    
admin.site.register(Post, PostAdmin)