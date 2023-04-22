from django.shortcuts import render, redirect
from django.db.models import Avg, Min

from book.models import Book


# Create your views here.
def index(request):
    books = Book.objects.all().order_by("title")
    num_of_books = books.count()
    average_ratings = books.aggregate(Avg("rating"), Min("rating"))
    context = {
        "title": "book list",
        "books": books,
        "total_books": num_of_books,
        "average_ratings": average_ratings,
    }
    return render(request, "book/index.html", context)


def detail(request, slug):
    try:
        book = Book.objects.get(slug=slug)
    except Book.DoesNotExist:
        return redirect("not-found")
    context = {
        "title": book.title,
        "is_bestseller": book.is_bestselling,
        "author": book.author,
        "rating": book.rating,
    }
    return render(request, "book/detail.html", context)
