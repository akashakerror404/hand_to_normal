from django.urls import path
from .views import ConvertTextView

urlpatterns = [
        path('convert/', ConvertTextView.as_view(), name='convert-text'),

]