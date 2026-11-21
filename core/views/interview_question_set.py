
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from core.models import InterviewQuestionSet
from core.serializers import InterviewQuestionSetSerializer


@api_view(['GET'])
def view_interview_questions(request, pk):
    interview_questions = InterviewQuestionSet.objects.filter(pk=pk).first()

    if interview_questions is None:
        return Response(
            {'error': 'Interview question set not found.'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = InterviewQuestionSetSerializer(interview_questions)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )
