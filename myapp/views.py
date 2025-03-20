from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import HandwrittenText
from .serializers import HandwrittenTextSerializer
import cv2
import numpy as np
import pytesseract

from paddleocr import PaddleOCR
import cv2
import numpy as np
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.response import Response
from rest_framework import status

class ConvertTextView(APIView):
    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get('image')
        if not image_file:
            return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Read image
        image_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
        image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)

        # Use PaddleOCR
        ocr = PaddleOCR(use_angle_cls=True, lang="en")
        result = ocr.ocr(image, cls=True)

        extracted_text = " ".join([line[1][0] for line in result[0]]) if result[0] else "No text detected"

        return Response({"text": extracted_text}, status=status.HTTP_200_OK)
