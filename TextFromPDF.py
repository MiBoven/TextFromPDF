import os
import PyPDF2

text = []
def extract_text_from_pdf(pdf_path):
    # Check if the file exists
    if os.path.exists(pdf_path):
        # open the pdf
        with open(pdf_path, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            # Get the text of every page
            for page_number in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_number]
                text.append(page.extract_text())
    else:
        print("File does not exist.")

#pdf_path = "files/example.pdf"
pdf_path = "files/spin.pdf"

extract_text_from_pdf(pdf_path)
if len(text) > 0:
    counter = 1
    for text in text:
        print("\n#### Page", counter, "####")
        print(text)
        counter += 1
