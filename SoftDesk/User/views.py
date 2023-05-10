from rest_framework import viewsets
from .models import User, Contributor
from .serializers import UserSerializer, ContributorSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = []

    def get_queryset(self):
        return Contributor.objects.all()