from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from .permissions import IsCommentAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated


class CommentViewSet(viewsets.ModelViewSet, IsCommentAuthorOrReadOnly):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsCommentAuthorOrReadOnly]
