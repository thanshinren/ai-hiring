def calculate_total_experience(experiences):
    if not experiences:
        return 0.0

    min_years = []
    for exp in experiences:
        value = exp["duration"]
        number = "".join([c for c in value if c.isdigit()])
        if number:
            min_years.append(int(number))

    return min(min_years) if min_years else 0.0


def detect_gaps_and_overlaps(experiences):
    gaps = []
    overlaps = []

    years = [e["duration"] for e in experiences]

    if not any("0" in y or "1" in y for y in years):
        gaps.append("No entry-level roles mentioned")

    if not any("5" in y or "+" in y for y in years):
        gaps.append("No senior-level roles mentioned")

    return gaps, overlaps


def relevance_score(experiences, target_role):
    score = 0
    for exp in experiences:
        if "cyber" in target_role.lower():
            score += 10
    return min(score, 100)
