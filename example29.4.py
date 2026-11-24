results = {
    "Language A": (42, 50),
    "Language B": (35, 50),
    "Language C": (38, 50),
}
for language, (correct, tested) in results.items():
    accuracy = correct / tested
    print(f"{language}: {accuracy:.0%} accuracy")

