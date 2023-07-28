from django.shortcuts import render
from django.http import HttpResponse
from docx import Document
from pdf2docx import Converter
import os
def convert_pdf_to_word(request):
    if request.method == 'POST' and request.FILES['pdf_file']:
        pdf_file = request.FILES['pdf_file']
        # Save the uploaded PDF file temporarily
        with open('temp.pdf', 'wb') as f:
            f.write(pdf_file.read())

        # Convert PDF to Word
        cv = Converter('temp.pdf')
        cv.convert('temp.docx', start=0, end=None)
        cv.close()

        # Load the converted Word document
        doc = Document('temp.docx')
        word_content = []
        for para in doc.paragraphs:
            word_content.append(para.text)
        # Delete the temporary files
        os.remove('temp.pdf')
        os.remove('temp.docx')
        # Return the converted Word document as a response
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename="converted.docx"'

        doc.save(response)
        return response

    return render(request, 'converter/index.html')