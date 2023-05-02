from django.shortcuts import render
from django.views import View


def store_files(file):
    with open("user_profile/static/image.jpg", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        return render(request, "user_profile/index.html")

    def post(self, request):
        file = request.FILES.get("file")
        store_files(file)
        return render(request, "user_profile/index.html")


# Create your views here.
