import re
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

STOPWORDS = set(stopwords.words('english'))

EDUCATION = [
    'BE', 'B.E.', 'B.E', 'BS', 'B.S', 'ME', 'M.E', 'M.E.', 'MBA', 'M.B.A', 
    'MS', 'M.S', 'BTECH', 'B.TECH', 'M.TECH', 'MTECH', 'SSC', 'HSC', 'CBSE', 
    'ICSE', 'X', 'XII'
]

def extract_education(resume_text):
    """
    Extract educational qualifications from the resume text.
    """
    sentences = resume_text.split('\n')
    qualifications = []
    for sentence in sentences:
        for word in sentence.split():
            word_clean = re.sub(r'[?|$|.|!|,]', r'', word)
            if word_clean.upper() in EDUCATION and word_clean not in STOPWORDS:
                qualifications.append(word_clean)
    return list(set(qualifications))
