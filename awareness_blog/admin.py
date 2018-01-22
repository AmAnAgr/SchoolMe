from django.contrib import admin
from .models import Post, Section

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "section", "published"]
    list_filter = ["section",]
    fields = [
        "section",
        "title",
        "slug",
        "author",
        "teaser",
        "content",
        "published",
    ]
    prepopulated_fields = {"slug": ("title",)}

class SectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Section, SectionAdmin)