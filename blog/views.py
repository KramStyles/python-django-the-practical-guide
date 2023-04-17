from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    context = {"title": "News"}
    return render(request, "blog/index.html", context)


def post(request):
    return redirect("blog-home")


def post_details(request):
    pass
