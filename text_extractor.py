import docx2txt
from PyPDF2 import PdfFileReader

def extract_text(file_path):
    """
    Extract text from a .pdf or .docx file.
    """
    if file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    elif file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    else:
        raise ValueError("Unsupported file format. Please upload a .docx or .pdf file.")

def extract_text_from_docx(file_path):
    """
    Extract text from a .docx file.
    """
    temp = docx2txt.process(file_path)
    resume_text = [line.replace('\t', ' ') for line in temp.split('\n') if line]
    return ' '.join(resume_text)

def extract_text_from_pdf(file_path):
    """
    Extract text from a .pdf file.
    """
    with open(file_path, 'rb') as pdf_file:
        reader = PdfFileReader(pdf_file)
        text = ''
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText()
    return text
