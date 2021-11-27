from django.contrib import admin

from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    class Meta:
        model = BlogPost
        
    readonly_fields = ("slug", "created", "modified")
    list_display = ["title", "category", "author", "is_published"]
