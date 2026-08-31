from rest_framework import serializers
from issues.models import Issue

class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "description",
            "status",
            "priority",
            "issue_type",
            "project",
            "assigned_to",
            "created_by",
            "created_at",
            "updated_at",
            "removed_at"
        ]

        read_only_fields = [
            "id",
            "created_by",
            "created_at",
            "updated_at",
        ]

    def validate_title(self, value):
        if len(value)<5:
            raise serializers.ValidationError(
                "Title must be atleast 5 letters long."
            )

        return value

    def validate(self, attrs):
        if self.instance is None and attrs.get("status")=="CLOSED":
            raise serializers.ValidationError(
                "A new issue cannot be created as CLOSED."
            )

        return attrs