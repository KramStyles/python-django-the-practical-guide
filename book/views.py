from django.shortcuts import render, redirect

from book.models import Book
from challenges.views import not_found_page


# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {"title": "book list", "books": books}
    return render(request, "book/index.html", context)


def detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return redirect("not-found")
    context = {
        "title": book.title,
        "is_bestseller": book.is_bestselling,
        "author": book.author,
        "rating": book.rating,
    }
    return render(request, "book/detail.html", context)
