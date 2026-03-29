from section_keywors import SECTION_KEYWORDS

def detect_sections_rule_based(text):
    sections = {}
    current_section = "others"
    sections[current_section] = []

    for line in text.split("\n"):
        clean_line = line.strip().lower().rstrip(":")

        found_heading = False
        for section, keywords in SECTION_KEYWORDS.items():
            if clean_line in keywords:
                current_section = section
                sections.setdefault(section, [])
                found_heading = True
                break

        if not found_heading:
            sections[current_section].append(line)

    return sections
