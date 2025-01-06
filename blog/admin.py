from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "is_published", "views")
    list_filter = ("title",)
    search_fields = (
        "title",
        "content",
    )
