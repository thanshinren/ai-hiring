ROLE_KEYWORDS = {
    "cybersecurity analyst": ["siem", "incident", "security", "soc"],
    "soc analyst": ["alerts", "monitoring", "siem"],
    "cloud security engineer": ["cloud", "aws", "iam", "cspm"]
}

def role_similarity(candidate_role, target_role):
    candidate_role = candidate_role.lower()
    target_role = target_role.lower()

    c_keywords = set()
    t_keywords = set()

    for role, keywords in ROLE_KEYWORDS.items():
        if role in candidate_role:
            c_keywords.update(keywords)
        if role in target_role:
            t_keywords.update(keywords)

    if not c_keywords or not t_keywords:
        return 0.2

    return round(len(c_keywords & t_keywords) / len(t_keywords), 2)
