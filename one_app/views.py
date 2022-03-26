from django.http import HttpResponse


def index(request):
    return HttpResponse("This is a hello post")


def show_age(request, age):
    # return HttpResponse(f"<h1>Age is {age + 2} </h1>")
    return HttpResponse("<h1>Age is %s </h1>" % (age + 2))
