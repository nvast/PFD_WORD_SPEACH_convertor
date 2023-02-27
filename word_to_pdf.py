import os
import win32com.client as win32

# "r" before string is necessery
file_path = r"replace with file path"

word = win32.gencache.EnsureDispatch('Word.Application')
doc = word.Documents.Open(f"{file_path}")

pdf_path = os.path.splitext(doc.FullName)[0] + '.pdf'
doc.SaveAs(pdf_path, FileFormat=17)

doc.Close()
word.Quit()
