from rest_framework import viewsets
from .serializers import IssueSerializer
from .permissions import IsIssueAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated
from Project.models import Project

# l'utilisateur ne doit pouvoir appliquer le processus CRUD aux problèmes
# du projet que si il ou elle figure sur la liste des contributeurs.

# Seuls les contributeurs sont autorisés à créer ou à consulter
# les problèmes d'un projet.


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsIssueAuthorOrReadOnly]

    def get_queryset(self):
        project_id = self.kwargs['project_pk']
        project = (Project.objects.filter(pk=project_id,
                                          project_contributor__user=self.request.user)
                   | Project.objects.filter(pk=project_id, author=self.request.user))

        return project[0].issue_related
