def generate_summary(test_results):
    return {
        "tests_analyzed": len(test_results),
        "normal_count": sum(1 for t in test_results if t["status"] == "Normal"),
        "low_count": sum(1 for t in test_results if t["status"] == "Low"),
        "high_count": sum(1 for t in test_results if t["status"] == "High"),
    }