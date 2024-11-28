import re

def extract_email_addresses(resume_text):
    """
    Extract email addresses from the resume text.
    """
    pattern = re.compile(r'[\w\.-]+@[\w\.-]+')
    return pattern.findall(resume_text)
