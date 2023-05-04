from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

from blog.forms import CommentForm
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

    def populate_context(self, comment_form, blog_instance):
        bookmarks = self.request.session.get("bookmarked")
        context = {
            "title": f"News Post: {blog_instance.title.title()}",
            "data": blog_instance,
            "comment_form": comment_form,
            "bookmarks": bookmarks,
        }
        return context

    def post(self, request, slug):
        blog = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(
                commit=False
            )  # To prevent the saving till we add post
            comment.post = blog
            comment.save()
            return redirect("blog-post-details", slug=slug)

        context = self.populate_context(comment_form=comment_form, blog_instance=blog)
        context.update(
            {
                "status": "error",
                "message": "An error occurred while saving comment. Check below!",
            }
        )
        return render(request, "blog/post_detail.html", context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            self.populate_context(comment_form=CommentForm(), blog_instance=self.object)
        )
        return context


class BookmarkView(View):
    def post(self, request):
        bookmark_id = int(request.POST.get("bookmark-id"))
        slug = request.POST.get("slug")

        # Get session
        bookmarked = request.session.get("bookmarked")
        if not bookmarked:
            bookmarked = []

        # Add id to session if it's not already there
        if bookmark_id not in bookmarked:
            bookmarked.append(bookmark_id)
        else:
            # unset it from bookmark
            bookmarked.remove(bookmark_id)

        request.session["bookmarked"] = bookmarked

        return redirect("blog-post-details", slug=slug)
