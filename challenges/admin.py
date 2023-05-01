from django.contrib import admin

from challenges.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ["username", "ratings"]


admin.site.register(Review, ReviewAdmin)
