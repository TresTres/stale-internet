from rest_framework import viewsets, permissions

from db_admin.themes.models import Theme
from db_admin.subjects.models import Subject, Comment
from db_admin.subjects.serializers import SubjectSerializer, CommentSerializer


class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    name = "subjects"


class CommentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    name = "comments"
