import json
import os

# -------------------------------------------------
# LOAD BENCHMARK RANGES
# -------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BENCHMARK_FILE = os.path.join(
    BASE_DIR, "benchmarks", "medical_ranges.json"
)

with open(BENCHMARK_FILE, "r") as f:
    MEDICAL_RANGES = json.load(f)


# -------------------------------------------------
# CONFIDENCE CALCULATION (NOT DIAGNOSTIC)
# -------------------------------------------------

def calculate_confidence(value, min_val, max_val):
    """
    Measures how clear the interpretation is,
    NOT medical certainty.
    """
    if value is None or min_val is None or max_val is None:
        return 0.3

    span = max_val - min_val
    if span <= 0:
        return 0.4

    if min_val <= value <= max_val:
        return 0.9

    distance = min(abs(value - min_val), abs(value - max_val))
    ratio = distance / span

    if ratio < 0.1:
        return 0.75
    elif ratio < 0.25:
        return 0.6
    else:
        return 0.45


# -------------------------------------------------
# MAIN ANALYSIS FUNCTION
# -------------------------------------------------

def analyze_tests(lab_values: dict):
    """
    Takes extracted lab values from parser

    Returns:
        test_results: list of structured test objects
        overall risk_score: int (0–100)
    """

    test_results = []
    total_risk_weight = 0

    for test_name, value in lab_values.items():

        # Skip tests without benchmarks
        if test_name not in MEDICAL_RANGES:
            continue

        range_info = MEDICAL_RANGES[test_name]

        # --- Extract range safely ---
        range_vals = range_info.get("range", [])
        if len(range_vals) == 2:
            min_val, max_val = range_vals
        else:
            min_val, max_val = None, None

        # --- Determine status ---
        if min_val is None or max_val is None:
            status = "Unknown"
            risk_weight = 0
            confidence = 0.3
        else:
            if value < min_val:
                status = "Low"
                risk_weight = 1          # ✅ changed
            elif value > max_val:
                status = "High"
                risk_weight = 1          # ✅ changed
            else:
                status = "Normal"
                risk_weight = 0

            confidence = calculate_confidence(value, min_val, max_val)

        # --- Append result ---
        test_results.append({
            "test": test_name,
            "value": value,
            "status": status,
            "normalRange": f"{min_val} – {max_val}" if min_val is not None else "Unknown",
            "confidence": confidence
        })

        total_risk_weight += risk_weight

    # -------------------------------------------------
    # Normalize risk score to 0–100
    # -------------------------------------------------
    max_possible = len(test_results) if test_results else 1
    risk_score = int((total_risk_weight / max_possible) * 100)

    return test_results, risk_score