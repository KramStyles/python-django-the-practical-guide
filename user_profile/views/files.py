from django.shortcuts import render, reverse
from django.views import View
from django.views.generic import FormView

from user_profile.forms import ProfileForm, ModelProfileForm


def store_files(file):
    with open(f"user_profile/static/{file.name}", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        return render(request, "user_profile/index.html")

    def post(self, request):
        file = request.FILES.get("file")
        store_files(file)
        return render(request, "user_profile/index.html")


class ProfileView(FormView):
    form_class = ProfileForm
    template_name = "user_profile/upload-form.html"
    success_url = "/profile/form-view/"

    def form_valid(self, form):
        file = form.files.get("user_image")
        store_files(file)
        return super().form_valid(form)


class ModelProfileView(FormView):
    form_class = ModelProfileForm
    template_name = "user_profile/model-form.html"
    success_url = "/profile/model-form-view/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
