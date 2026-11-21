
from pathlib import Path

from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from core.serializers import ResumeSerializer


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_resume(request):
    file = request.FILES.get('file')

    if not file:
        return Response(
            {'error': 'Resume file is required.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    allowed_extensions = ['.pdf', '.docx', '.txt']

    if Path(file.name).suffix.lower() not in allowed_extensions:
        return Response(
            {'error': 'Only PDF, DOCX and TXT files are allowed.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = ResumeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )
