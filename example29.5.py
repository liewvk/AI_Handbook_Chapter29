weights = {"accuracy": 0.40, "speed": 0.20,
           "privacy": 0.25, "cost": 0.15}
models = {
    "Local model": {"accuracy": 7, "speed": 8, "privacy": 9, "cost": 9},
    "Cloud model": {"accuracy": 9, "speed": 8, "privacy": 6, "cost": 6},
}
for name, scores in models.items():
    total = sum(weights[k] * scores[k] for k in weights)
    print(f"{name}: {total:.2f} / 10")

