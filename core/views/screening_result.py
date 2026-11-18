
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import ScreeningResult
from core.serializers import ScreeningResultSerializer


class ViewScreeningResultAPIView(APIView):

    def get(self, request, pk):
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
