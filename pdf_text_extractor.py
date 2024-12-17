import PyPDF2
from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as pdf_file:
        reader = PdfReader(file_path)

        num_pages = reader.numPages
        text = ''
        for page in range(num_pages):
            page_obj = reader.getPage(page)
            text += page_obj.extractText()

        return text

def main():
    file_path = "AQA GCSE textbook.pdf"
    text = extract_text_from_pdf(file_path)

    if text is not None:
        print(text)

if __name__ == "__main__":
    main()