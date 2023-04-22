from django.shortcuts import render

from book.models import Book


# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {"title": "book list", "books": books}
    return render(request, "book/index.html", context)
