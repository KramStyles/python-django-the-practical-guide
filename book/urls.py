from django.urls import path

from book import views

urlpatterns = [
    path("book/", views.index, name="book-list"),
    path("book/<slug:slug>", views.detail, name="book-detail"),
]
