
from rest_framework import serializers
from core.models import JobPosition


class JobPositionSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(
        source='department.name',
        read_only=True
    )

    class Meta:
        model = JobPosition
        fields = [
            'id',
            'department',
            'department_name',
            'title',
            'description',
            'required_skills',
            'created_at'
        ]
        read_only_fields = [
            'id',
            'department_name',
            'created_at'
        ]

    def validate_required_skills(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError(
                "Required skills must be a list of strings."
            )

        if not all(isinstance(skill, str) for skill in value):
            raise serializers.ValidationError(
                "Every skill must be a string."
            )

        return value
