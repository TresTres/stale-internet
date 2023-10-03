from rest_framework import viewsets, permissions

from db_admin.reactions.models import Reaction, ReactionCategory
from db_admin.reactions.serializers import (
    ReactionSerializer,
    ReactionCategorySerializer,
)


class ReactionCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ReactionCategory.objects.all()
    serializer_class = ReactionCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    name = "reaction-categories"


class ReactionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    name = "reactions"
