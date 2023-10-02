from django.urls import include, path
from rest_framework import routers
from db_admin.themes import views 

router = routers.DefaultRouter()
router.register(r'themes', views.ThemeViewSet)

urlpatterns = [
    path('', include(router.urls)), 
]