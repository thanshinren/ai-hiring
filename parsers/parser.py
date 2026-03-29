import re
from parser.skill_mapper import SKILL_SYNONYMS, ROLE_VARIATIONS
import re

def extract_roles(text):
    roles_found = set()

    # 1️⃣ Explicit role titles (recommended list)
    role_keywords = [
        "cybersecurity analyst",
        "information security analyst",
        "security analyst",
        "soc analyst",
        "cloud security engineer",
        "cloud security analyst",
        "incident response lead",
        "security operations lead",
        "cyber defense lead",
        "cybersecurity consultant",
        "soc consultant",
        "security consultant",
        "intern"
    ]

    for role in role_keywords:
        if role in text:
            roles_found.add(role)

    
    numbered_roles = re.findall(
        r"\b\d+\.\s*([A-Za-z ]+Analyst|[A-Za-z ]+Engineer|[A-Za-z ]+Lead|Intern)\b",
        text
    )

    for r in numbered_roles:
        roles_found.add(r.strip().lower())

    return sorted(roles_found)



'''def extract_skills(text):
    skills_found = set()
    for skill, synonyms in SKILL_SYNONYMS.items():
        if skill in text:
            skills_found.add(skill)
        for s in synonyms:
            if s in text:
                skills_found.add(skill)
    return list(skills_found)'''
SKILL_LIST = ["SIEM","EDR","IDS","IPS","Firewall","Network Security","Cloud Security","Incident Response","Threat Detection",
"Vulnerability Management","Malware Analysis","Penetration Testing","Risk Assessment"
]

def extract_skills(text):
    skills_found = []
    for skill in SKILL_LIST:
        if skill in text:
            skills_found.append(skill)
    return list(set(skills_found))

import re

def extract_experience(text):
    pattern = r"\b\d+\s*(?:\+|\-\d+)?\s*years\b"
    matches = re.findall(pattern, text)
    return matches

def normalise_experience(experience_list):
    normalized = set()

    for exp in experience_list:
        exp = exp.replace("\u2013", "-").replace("\u2014", "-")
        exp = exp.replace("to", "-")
        exp = exp.strip()
        normalized.add(exp)

    return sorted(normalized)

def extract_education(text):
    education_map = {
        "bachelor": "bachelor degree",
        "master": "master degree",
        "degree": "degree",
        "cybersecurity": "cybersecurity background",
        "computer science": "computer science"
    }

    education = set()
    for key, value in education_map.items():
        if key in text:
            education.add(value)

    return list(education)

def parse_jd(normalized_text):
    raw_exp = extract_experience(normalized_text)

    return {
        "roles": extract_roles(normalized_text),
        "skills": extract_skills(normalized_text),
        "experience_required": normalise_experience(raw_exp),
        "education_preferences": extract_education(normalized_text)
    }

    

