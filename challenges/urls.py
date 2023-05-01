from django.urls import path
from challenges import views

urlpatterns = [
    path("<int:day>", views.daily_challenge_by_number),
    path("<str:day>", views.index, name="weekly-activities"),
    path("", views.challenge_home, name="challenges-home"),
    path("404/", views.not_found_page, name="not-found"),
    path("reviews/", views.reviews, name="reviews"),
    path("reviews-class/", views.Reviews.as_view(), name="reviews-class"),
]
