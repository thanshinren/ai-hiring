def load_labeled_data(file_path):
    data = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if "||" not in line:
                continue

            text, label = line.split("||")
            text = text.strip()
            label = label.strip().lower()

            if text and label:
                data.append((text, label))

    return data

