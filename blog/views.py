from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from blog.models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by("-updated_at")[:6]
    context = {"title": "News", "posts": posts}
    return render(request, "blog/index.html", context)


def post(request):
    return redirect("blog-home")


def post_details(request, slug):
    blog = get_object_or_404(Post, slug=slug)
    context = {
        "title": f"News Post: {blog.title.title()}",
        "data": blog,
    }
    return render(request, "blog/post_detail.html", context)


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = ["-updated_at"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "News"
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        # return queryset.order_by("-updated_at")[:6]
        return queryset[:6]


class PostDetailView(DetailView):
    model = Post
    context_object_name = "data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_title = self.object.title.title()
        context["title"] = f"News Post: {post_title}"
        return context
