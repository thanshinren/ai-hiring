from datetime import datetime

MONTHS = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4,
    "may": 5, "jun": 6, "jul": 7, "aug": 8,
    "sep": 9, "oct": 10, "nov": 11, "dec": 12
}

def parse_date(text):
    text = text.lower().strip().replace("–", "-")

    if "present" in text:
        return datetime.today()

    parts = text.split()
    if len(parts) < 2:
        return None

    month = MONTHS.get(parts[0][:3])
    year = int(parts[1])

    return datetime(year, month, 1)

def months_between(start, end):
    return (end.year - start.year) * 12 + (end.month - start.month)
