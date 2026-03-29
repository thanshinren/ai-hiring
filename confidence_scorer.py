def calculate_confidence(skill, frequency, category):
    score = 0.4

    # Frequency boost
    score += min(frequency * 0.1, 0.4)

    # Category weight
    if category in ["tools", "frameworks"]:
        score += 0.2
    elif category == "certifications":
        score += 0.3

    return round(min(score, 1.0), 2)
