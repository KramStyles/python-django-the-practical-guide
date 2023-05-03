from django.shortcuts import render, reverse
from django.views import View
from django.views.generic import FormView, CreateView, ListView, DetailView

from user_profile.forms import ProfileForm, ModelProfileForm
from user_profile.models import UserProfile


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
    success_url = "/profile/user-profiles/"

    def form_valid(self, form):
        file = form.files.get("user_image")
        store_files(file)
        return super().form_valid(form)


class ModelProfileView(FormView):
    form_class = ModelProfileForm
    template_name = "user_profile/model-form.html"
    success_url = "/profile/user-profiles/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserProfileCreateView(CreateView):
    """This is same to the ModelProfileView but shorter. No need for forms"""

    template_name = "user_profile/model-form.html"
    success_url = "/profile/user-profiles/"
    model = UserProfile
    # fields = "__all__"
    form_class = ModelProfileForm


class UserProfileListView(ListView):
    model = UserProfile
    template_name = "user_profile/user-profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "User Profiles"
        return context


class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = "user_profile/user-profile-detail.html"
    context_object_name = "profile"
