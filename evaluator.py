from classifier import classify_section

def evaluate_classifier(labeled_data):
    correct = 0
    results = []

    for text, true_label in labeled_data:
        predicted = classify_section(text)

        if predicted == true_label:
            correct += 1

        results.append((text, true_label, predicted))

    accuracy = (correct / len(labeled_data)) * 100 if labeled_data else 0
    return accuracy, results
