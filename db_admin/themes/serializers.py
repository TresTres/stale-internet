from rest_framework import serializers

from django.contrib.auth.models import User

from db_admin.themes.models import Theme


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_active", "date_joined", "groups"]


class ThemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Theme
        fields = "__all__"
