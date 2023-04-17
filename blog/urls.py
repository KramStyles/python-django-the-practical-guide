from django.urls import path

from blog import views

urlpatterns = [
    path("", views.index, name="blog-home"),
    path("posts/", views.post, name="blog-post"),
    path("posts/<slug:slug>/", views.post_details, name="blog-post-details"),
]
