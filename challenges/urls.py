from django.urls import path
from challenges import views

urlpatterns = [
    path("<int:day>", views.daily_challenge_by_number),
    path("<str:day>", views.index, name="weekly-activities"),
    path("", views.challenge_home, name="challenges-home"),
]