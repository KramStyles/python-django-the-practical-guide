from django.urls import path

from user_profile import views

urlpatterns = [
    path("", views.CreateProfileView.as_view(), name="create-profile"),
    path("form-view/", views.ProfileView.as_view(), name="form-profile"),
    path("model-form-view/", views.ModelProfileView.as_view(), name="model-profile"),
    path("create-form-view/", views.UserProfileCreateView.as_view(), name="user-profile-create-view"),
    path("user-profiles/", views.UserProfileListView.as_view(), name="user-profile-list-view"),
    path("user-detail/<int:pk>/", views.UserProfileDetailView.as_view(), name="user-profile-detail-view"),
]
