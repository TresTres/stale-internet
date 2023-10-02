from rest_framework import viewsets, permissions

from db_admin.themes.models import Theme
from db_admin.themes.serializers import ThemeSerializer
class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    permission_classes = [permissions.IsAuthenticated]
    name = 'themes'
