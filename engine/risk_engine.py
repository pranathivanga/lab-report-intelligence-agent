def calculate_risk_score(lab_values, benchmarks):
    total_score = 0
    detailed_scores = {}

    for test, value in lab_values.items():
        if test not in benchmarks:
            continue

        benchmark = benchmarks[test]
        normal_min, normal_max = benchmark["range"]
        weight = benchmark["severity_weight"]

        # Default: no risk
        contribution = 0
        deviation_pct = 0

        if value < normal_min:
            deviation_pct = (normal_min - value) / normal_min
        elif value > normal_max:
            deviation_pct = (value - normal_max) / normal_max

        # Scoring logic (simple & explainable)
        if deviation_pct > 0:
            if deviation_pct > 0.3:
                contribution = weight * 2
            elif deviation_pct > 0.2:
                contribution = weight * 1.5
            elif deviation_pct > 0.1:
                contribution = weight

        total_score += contribution

        detailed_scores[test] = {
            "value": value,
            "normal_range": benchmark["range"],
            "deviation_percent": round(deviation_pct * 100, 1),
            "score_contribution": round(contribution, 1)
        }

    # Cap score at 100
    total_score = min(round(total_score, 1), 100)

    # Risk label
    if total_score < 20:
        risk_level = "Low"
    elif total_score < 50:
        risk_level = "Moderate"
    else:
        risk_level = "High"

    return total_score, risk_level, detailed_scores