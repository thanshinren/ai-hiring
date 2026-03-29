from labeleed_samples import load_labeled_data
from evaluator import evaluate_classifier

labeled_data = load_labeled_data("data/extracted_text.txt")

print("Loaded samples:", len(labeled_data))
print(labeled_data[:5])

accuracy, results = evaluate_classifier(labeled_data)

print("Accuracy:", accuracy)
print("\nSample Results:")
for r in results[:5]:
    print(r)
