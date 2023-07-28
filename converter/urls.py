from django.urls import path
from .views import convert_pdf_to_word

app_name = 'converter'

urlpatterns = [
    path('', convert_pdf_to_word, name='convert_pdf_to_word'),
]
