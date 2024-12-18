from PyPDF2 import PdfReader

# Load PDF
reader = PdfReader("AQA GCSE textbook.pdf")

# Extract text from each page
for page in reader.pages:
    print(page.extract_text())
