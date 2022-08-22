from django.urls import path
from . import views

urlpatterns = [
    path('', views.RanksList.as_view()),
]
