import pandas as pd
import spacy

nlp = spacy.load('en_core_web_sm')

def extract_skills(resume_text):
    """
    Extract technical skills from the resume text using a predefined skills list.
    """
    nlp_text = nlp(resume_text)
    tokens = [token.text.lower() for token in nlp_text if not token.is_stop]
    skills = pd.read_csv('skills.csv')['Skill'].str.lower().tolist()  # Load skills from CSV
    skillset = [token.capitalize() for token in tokens if token in skills]
    return list(set(skillset))
