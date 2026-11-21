
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from core.models import ScreeningResult
from core.serializers import ScreeningResultSerializer


@api_view(['GET'])
def view_screening_result(request, pk):
    screening_result = ScreeningResult.objects.filter(pk=pk).first()

    if screening_result is None:
        return Response(
            {'error': 'Screening result not found.'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ScreeningResultSerializer(screening_result)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )
