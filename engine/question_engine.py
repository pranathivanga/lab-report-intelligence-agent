def generate_questions(test_results: list, patterns: list) -> list:
    questions = []

    for test in test_results:
        if test["status"] in ("low", "high"):
            questions.append(
                f"What could be possible reasons for my {test['test_name']} being {test['status']}?"
            )
            questions.append(
                f"Should the {test['test_name']} test be repeated to confirm this result?"
            )

    for pattern in patterns:
        desc = pattern.get("description")
        if desc:
            questions.append(
                f"Is there any clinical significance to the pattern involving {desc}?"
            )

    # Deduplicate while preserving order
    seen = set()
    unique = []
    for q in questions:
        if q not in seen:
            seen.add(q)
            unique.append(q)

    return unique