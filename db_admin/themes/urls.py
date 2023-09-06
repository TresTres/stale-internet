from django.urls import path
from themes import views

urlpatterns = [
    path("", views.index, name="themes_index"),
]