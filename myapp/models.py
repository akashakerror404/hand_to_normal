from django.db import models

# Create your models here.
from django.db import models

class HandwrittenText(models.Model):
    image = models.ImageField(upload_to='handwritten_images/')
    digital_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"