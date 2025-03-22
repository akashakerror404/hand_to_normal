from django.urls import path
from .views import convert_text_view

urlpatterns = [
        path('', convert_text_view, name='convert-text'),

]