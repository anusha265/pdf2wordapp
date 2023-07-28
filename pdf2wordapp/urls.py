from django.urls import path, include
from converter.views import convert_pdf_to_word

urlpatterns = [
    path('', convert_pdf_to_word, name='convert_pdf_to_word'),
    path('', include('converter.urls')),
]
