"""
URL configuration for db_admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# from db_admin.themes.urls import urlpatterns as theme_api_urlpatterns
# from db_admin.subjects.urls import urlpatterns as subject_api_urlpatterns

from rest_framework import routers
from db_admin.subjects import views as subject_views 
from db_admin.themes import views as theme_views

router = routers.DefaultRouter()
router.register(r'users', theme_views.UserViewSet)
router.register(r'themes', theme_views.ThemeViewSet)
router.register(r'subjects', subject_views.SubjectViewSet)
router.register(r'comments', subject_views.CommentViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
