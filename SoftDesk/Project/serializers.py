from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    project_contributor = serializers.StringRelatedField(many=True)

    class Meta:

        model = Project
        fields = ['id',
                  'title',
                  'description',
                  'type',
                  'author',
                  'issue_related',
                  'project_contributor',
                  ]
        read_only_fields = ("author",)

    def create(self, validated_data):
        author = self.context.get("request", None).user  # récupère le token

        project = Project.objects.create(
            title=validated_data["title"],
            description=validated_data["description"],
            type=validated_data["type"],
            author=author
        )
        project.save()

        return project
