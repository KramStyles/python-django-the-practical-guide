from django.contrib import admin

from book.models import Book


class BookAdmin(admin.ModelAdmin):
    # Taking this out because of pre-population
    # readonly_fields = ("slug", )
    prepopulated_fields = {"slug": ("title", "author")}


admin.site.register(Book, BookAdmin)
