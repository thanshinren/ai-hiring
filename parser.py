import re

def parse_experience(text):
    """
    Extracts experience REQUIREMENTS from Job Description
    """
    experience_patterns = re.findall(
        r"(\d+\s*[–\-]\s*\d+\+?\s*years|\d+\+?\s*years)",
        text,
        flags=re.IGNORECASE
    )

    roles = []
    for line in text.split("\n"):
        if "analyst" in line.lower() or "engineer" in line.lower():
            roles.append(line.strip())

    experience_details = []
    for exp in experience_patterns:
        experience_details.append({
            "role": "Cybersecurity-related role",
            "company": "N/A (Job Requirement)",
            "duration": exp
        })

    return experience_details
