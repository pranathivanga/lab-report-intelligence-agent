import json

def load_benchmarks():
    with open("benchmarks/medical_ranges.json", "r") as f:
        return json.load(f)