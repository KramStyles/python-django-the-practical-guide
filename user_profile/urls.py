from django.urls import path

from user_profile import views

urlpatterns = [
    path("", views.CreateProfileView.as_view(), name="create-profile"),
]
