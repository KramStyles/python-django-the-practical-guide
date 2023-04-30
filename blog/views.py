from django.shortcuts import render, redirect, get_object_or_404

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
    return render(request, "blog/post-detail.html", context)
