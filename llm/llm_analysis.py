def analyze_commit(commit_message):

    risky_keywords = {
        "temporary": 0.15,
        "workaround": 0.20,
        "crash": 0.20,
        "memory leak": 0.20,
        "urgent": 0.10,
        "hotfix": 0.15,
        "rollback": 0.15,
        "quick patch": 0.15,
        "bypass": 0.10
    }

    score = 0.1

    detected_patterns = []

    explanation = []

    commit_lower = commit_message.lower()

    for keyword, weight in risky_keywords.items():

        if keyword in commit_lower:

            score += weight

            detected_patterns.append(keyword)

            explanation.append(
                f"Detected risky keyword: {keyword}"
            )

    score = min(score, 1.0)

    return {
        "semantic_risk_score": round(score, 2),
        "detected_patterns": detected_patterns,
        "analysis": explanation
    }