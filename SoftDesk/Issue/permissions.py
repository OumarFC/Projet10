from rest_framework import permissions

# Seuls les contributeurs sont autorisés à créer ou à consulter les problèmes
# d'un projet.

# En outre, ils ne peuvent les actualiser (Update) et les supprimer (Delete)
# que s'ils en sont les auteurs.


class IsIssueAuthorOrReadOnly(permissions.BasePermission):
    message = "Seul l'auteur du problème peut le modifier ou le supprimer"

    def has_object_permission(self, request, view,  obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
