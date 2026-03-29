from text_cleaner import clean_text
from skill_extractor import extract_skills
from confidence_scorer import calculate_confidence

# Example input (replace with PDF extracted text)
with open("data/extracted_text.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

cleaned_text = clean_text(raw_text)
skills = extract_skills(cleaned_text)

final_output = []

for skill, data in skills.items():
    confidence = calculate_confidence(
        skill,
        data["count"],
        data["category"]
    )

    final_output.append({
        "skill": skill,
        "category": data["category"],
        "frequency": data["count"],
        "confidence": confidence
    })

# Sort by confidence
final_output = sorted(final_output, key=lambda x: x["confidence"], reverse=True)

for s in final_output:
    print(s)
