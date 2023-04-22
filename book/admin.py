from django.contrib import admin

from book.models import Book, Author


class BookAdmin(admin.ModelAdmin):
    # Taking this out because of pre-population
    # readonly_fields = ("slug", )
    prepopulated_fields = {"slug": ("title", "author")}
    list_filter = ("author", "rating")
    list_display = ("title", "author")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
