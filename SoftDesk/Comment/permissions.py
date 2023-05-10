from rest_framework import permissions


class IsCommentAuthorOrReadOnly(permissions.BasePermission):
    message = "Seul l'auteur du commentaire peut actualiser ou supprimer"
    # Les commentaires doivent être visibles par tous les contributeurs au projet
    # et par le responsable du projet, mais seul leur auteur
    # peut les actualiser ou les supprimer.

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
