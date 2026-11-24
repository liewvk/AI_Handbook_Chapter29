observed = [10.0, 12.0, 11.0, 15.0]
baseline = [11.0, 11.0, 11.0, 11.0]
model = [10.5, 11.8, 11.4, 14.6]
def mae(actual, predicted):
    return sum(abs(a - b) for a, b in zip(actual, predicted)) / len(actual)
print(f"Baseline MAE: {mae(observed, baseline):.2f}")
print(f"Model MAE: {mae(observed, model):.2f}")

