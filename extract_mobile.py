import re

def extract_mobile_number(resume_text):
    """
    Extract mobile number from the resume text.
    """
    pattern = re.compile(r'\+?\d[\d -]{8,}\d')
    match = pattern.search(resume_text)
    return match.group() if match else "Mobile number not found"
