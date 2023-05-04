from django.urls import path

from blog import views

urlpatterns = [
    path("posts/bookmark/", views.BookmarkView.as_view(), name="bookmark-view"),
    path("", views.PostListView.as_view(), name="blog-home"),
    path("posts/<slug:slug>/", views.PostDetailView.as_view(), name="blog-post-details"),
    path("posts_function/", views.post, name="blog-post-function"),
    path("posts_function/<slug:slug>/", views.post_details, name="blog-post-details-function"),
]
