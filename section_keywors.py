import re

SECTION_KEYWORDS = {
    "skills": [
        "python", "sql", "machine learning", "cloud", "aws",
        "networking", "linux", "security", "endpoint"
    ],
    "experience": [
        "experience", "worked", "responsibilities",
        "engineer", "analyst", "developer", "years"
    ],
    "education": [
        "b.tech", "bachelor", "master", "degree",
        "university", "college", "education"
    ],
    "certifications": [
        "certified", "certification", "aws certified",
        "ceh", "security+", "cissp"
    ],
    "projects": [
        "project", "developed", "built", "implemented"
    ],
    "others": []
}

def classify_section(text):
    text = text.lower()

    # Experience year detection
    if re.search(r"\d+\s*[-–]?\s*\d*\s*years?", text):
        return "experience"

    for section, keywords in SECTION_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                return section

    return "others"

