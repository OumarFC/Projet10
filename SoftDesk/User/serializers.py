from rest_framework import serializers
from .models import Contributor, User
from Project.models import Project


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('id',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'is_active',
                  'is_admin',
                  'issue_created_by',
                  'issue_assigned_to',
                  'project_created_by',
                  'user_comment',
                  'user_contributor',
                  )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()
        return user


class ContributorSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Contributor
        fields = ('id',
                  'user',
                  'project',
                  )

    def validate_user(self, value):
        user = self.context['request'].user
        if user == value:
            raise serializers.ValidationError(
                "L'auteur du projet ne peut pas être contributeur")
        return value

    def create(self, validated_data):
        projet = Project.objects.get(pk=self.context.get("view").kwargs["project_pk"])

        contributor = Contributor.objects.create(
            user=validated_data["user"],
            project=projet
        )
        contributor.save()
        return contributor
