def detect_patterns(test_results, benchmarks):
    """
    test_results: list of test result objects
    benchmarks: medical ranges
    """

    patterns = []

    for test in test_results:
        name = test["test"]
        status = test["status"]

        if status == "low":
            patterns.append(f"{name} is lower than the typical range.")
        elif status == "high":
            patterns.append(f"{name} is higher than the typical range.")

    return patterns