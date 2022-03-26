from django.urls import path
from one_app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('age/<int:age>', views.show_age, name='age')
]