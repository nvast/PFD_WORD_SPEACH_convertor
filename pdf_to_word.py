import PyPDF2
import docx


with open('sample.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()


    doc = docx.Document()
    doc.add_paragraph(text)
    doc.save('sample.docx')

