import cv2
import numpy as np
import os
from paddleocr import PaddleOCR
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

def convert_text_view(request):
    extracted_text = None
    image_url = None  

    if request.method == "POST" and request.FILES.get("image"):
        image_file = request.FILES["image"]
        
        # Read file content once
        file_content = image_file.read()

        # Save uploaded image temporarily
        image_path = os.path.join(settings.MEDIA_ROOT, "uploaded_image.jpg")
        default_storage.save(image_path, ContentFile(file_content))
        image_url = settings.MEDIA_URL + "uploaded_image.jpg"

        # Convert image to OpenCV format
        image_bytes = np.frombuffer(file_content, dtype=np.uint8)  # Convert bytes to numpy array
        image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)  # Decode image

        if image is None:
            extracted_text = "Invalid image format or corrupted file."
        else:
            # Use PaddleOCR
            ocr = PaddleOCR(use_angle_cls=True, lang="en")
            result = ocr.ocr(image, cls=True)
            extracted_text = " ".join([line[1][0] for line in result[0]]) if result[0] else "No text detected"

    return render(request, "convert_text.html", {"extracted_text": extracted_text, "image_url": image_url})
