from datetime import date
items = [
    {"claim": "Data center demand may reach 945 TWh by 2030",
     "type": "forecast", "source": "IEA Energy and AI (2025)"},
    {"claim": "AI Index 2026 reports increased organizational adoption",
     "type": "reported finding", "source": "Stanford AI Index 2026"},
]
for item in items:
    print(f"[{item['type']}] {item['claim']}")
    print(f"Source: {item['source']}; checked: {date(2026, 11, 22)}")

