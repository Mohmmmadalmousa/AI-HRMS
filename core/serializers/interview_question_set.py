
from rest_framework import serializers
from core.models import InterviewQuestionSet


class InterviewQuestionSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewQuestionSet
        fields = '__all__'
        read_only_fields = [
            'id', 'candidate', 'job_position', 'screening_result',
            'technical_questions', 'behavioral_questions',
            'follow_up_questions', 'generated_at'
        ]
