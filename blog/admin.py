from django.contrib import admin

from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", ), "excerpt": ("content", )}
    list_filter = ("author", "tags", "updated_at")
    list_display = ("title", "author", "updated_at")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_email", "post")


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
