import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)

def extract_name(resume_text):
    """
    Extract candidate's name from the resume text.
    """
    nlp_text = nlp(resume_text)
    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]  # Proper nouns
    matcher.add('NAME', [pattern])
    matches = matcher(nlp_text)
    for _, start, end in matches:
        return nlp_text[start:end].text
    return "Name not found"
