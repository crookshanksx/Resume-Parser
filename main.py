from text_extractor import extract_text
from extract_name import extract_name
from extract_mobile import extract_mobile_number
from extract_email import extract_email_addresses
from extract_education import extract_education
from extract_skills import extract_skills

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    text = extract_text(file_path)

    print("Name:", extract_name(text))
    print("Mobile Number:", extract_mobile_number(text))
    print("Email Address:", extract_email_addresses(text))
    print("Qualifications:", extract_education(text))
    print("Skills:", extract_skills(text))
