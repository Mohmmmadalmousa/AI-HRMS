
from rest_framework import serializers
from core.models import ScreeningResult


class ScreeningResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreeningResult
        fields = '__all__'
        read_only_fields = [
            'id', 'candidate', 'job_position', 'score',
            'strengths', 'missing_skills', 'recommendation',
            'summary', 'raw_report', 'generated_at'
        ]
