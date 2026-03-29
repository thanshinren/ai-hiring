from collections import defaultdict
from skill_dictionary import SKILL_DICTIONARY
from normaliser import normalize_skill

def extract_skills(text):
    extracted = defaultdict(lambda: {"count": 0, "category": ""})

    for category, groups in SKILL_DICTIONARY.items():
        for group, keywords in groups.items():
            for keyword in keywords:
                if keyword in text:
                    skill_name = normalize_skill(keyword)
                    extracted[skill_name]["count"] += 1
                    extracted[skill_name]["category"] = category

    return extracted
