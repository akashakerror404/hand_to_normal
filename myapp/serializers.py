from rest_framework import serializers
from .models import HandwrittenText

class HandwrittenTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandwrittenText
        fields = ['id', 'image', 'digital_text', 'created_at']