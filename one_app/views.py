from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    info = {
        'message': "This is a message"
    }
    return render(request, 'one_app/index.html', context=info)


def show_age(request, age):
    # return HttpResponse(f"<h1>Age is {age + 2} </h1>")
    return HttpResponse("<h1>Age is %s </h1>" % (age + 2))
