from django.contrib import admin

from blog.models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", ), "excerpt": ("content", )}
    list_filter = ("author", "tags", "updated_at")
    list_display = ("title", "author", "updated_at")


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
