from django.urls import path

from user_profile import views

urlpatterns = [
    path("", views.CreateProfileView.as_view(), name="create-profile"),
    path("form-view/", views.ProfileView.as_view(), name="form-profile"),
    path("model-form-view/", views.ModelProfileView.as_view(), name="model-profile"),
]
