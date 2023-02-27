import pyttsx3
import PyPDF2

file = 'sample.pdf'


with open(file, 'rb') as pdf_file:

    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

# Make reading fluent
text = text.replace("\n", " ")


engine = pyttsx3.init()
# Set reading speed to be understandable
engine.setProperty("rate", 150)

engine.say(text)
engine.runAndWait()








