from text_preprocessor import preprocess_text
from nlp_based_classifier import classify_line

def detect_resume_sections(text):
    text = preprocess_text(text)

    final_sections = {
        "skills": [],
        "experience": [],
        "education": [],
        "certifications": [],
        "projects": [],
        "others": []
    }

    for line in text.split("\n"):
        clean_line = line.strip()
        if not clean_line:
            continue

        section = classify_line(clean_line)
        final_sections[section].append(clean_line)

    return final_sections
