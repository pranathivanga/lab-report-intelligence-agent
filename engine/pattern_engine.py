def detect_patterns(lab_values, benchmarks):
    pattern_hits = {}
    pattern_results = []

    # Group abnormal tests by pattern
    for test, value in lab_values.items():
        if test not in benchmarks:
            continue

        benchmark = benchmarks[test]
        normal_min, normal_max = benchmark["range"]
        pattern = benchmark["pattern_group"]

        is_abnormal = value < normal_min or value > normal_max

        if is_abnormal:
            pattern_hits.setdefault(pattern, []).append(test)

    # Decide patterns
    for pattern, tests in pattern_hits.items():
        if len(tests) >= 2:
            confidence = min(50 + len(tests) * 15, 90)
            pattern_results.append({
                "pattern": f"Possible {pattern}",
                "tests_involved": tests,
                "confidence_percent": confidence
            })

    return pattern_results