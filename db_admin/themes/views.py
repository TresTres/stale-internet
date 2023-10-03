from rest_framework import viewsets, permissions

from django.contrib.auth.models import User

from db_admin.themes.models import Theme
from db_admin.themes.serializers import ThemeSerializer, UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    name = "users"


class ThemeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    permission_classes = [permissions.IsAuthenticated]
    name = "themes"
