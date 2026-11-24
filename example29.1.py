models = {"3B": 3_000_000_000, "7B": 7_000_000_000}
for name, parameters in models.items():
    for bits in (16, 8, 4):
        gib = parameters * bits / 8 / (1024 ** 3)
        print(f"{name} at {bits} bits: {gib:.2f} GiB")

