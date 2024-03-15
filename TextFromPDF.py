import os
import PyPDF2

text = []
def extract_text_from_pdf(pdf_path):
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as f:
            ### TODO: bug fix here!
            pdf_reader = PyPDF2.PdfFileReader(f)
            for page_number in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_number)
                text.append(page.extractText())
    else:
        print("File does not exist")

pdf_path = "files/spin.pdf"

extract_text_from_pdf(pdf_path)
if len(text) > 0:
    for t in text:
        print(text[t])
