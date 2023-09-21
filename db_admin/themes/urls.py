from django.urls import path
from db_admin.themes import views

urlpatterns = [
    path("", views.index, name="themes_index"),
]