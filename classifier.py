def classify_section(text: str) -> str:
    if not text or not isinstance(text, str):
        return "other"

    t = text.lower().strip()

    # -------- ROLE TITLES (HIGHEST PRIORITY) --------
    role_keywords = [
        "analyst", "engineer", "consultant", "intern",
        "soc", "security", "forensics", "threat"
    ]
    if any(k in t for k in role_keywords) and len(t.split()) <= 6:
        return "role"

    # -------- SKILLS --------
    skills_keywords = [
        "siem", "splunk", "qradar", "sentinel",
        "linux", "windows", "network", "tcp/ip",
        "endpoint", "cloud", "edr", "soar", "mitre",
        "python", "firewall", "ids", "ips"
    ]
    if any(k in t for k in skills_keywords):
        return "skills"

    # -------- EXPERIENCE --------
    experience_keywords = [
        "monitor", "investigate", "analyze", "respond",
        "implement", "manage", "conduct", "perform",
        "triage", "escalate"
    ]
    if any(k in t for k in experience_keywords):
        return "experience"

    # -------- EDUCATION --------
    if any(k in t for k in ["bachelor", "degree", "university", "college"]):
        return "education"

    # -------- CERTIFICATIONS --------
    if any(k in t for k in ["certification", "security+", "ceh", "cissp", "cysa", "gcih"]):
        return "certifications"

    # -------- SUMMARY --------
    if len(t.split()) > 10:
        return "summary"

    return "other"
