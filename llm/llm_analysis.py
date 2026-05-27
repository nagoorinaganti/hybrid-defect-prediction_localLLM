def analyze_commit(commit_message):

    risk_keywords = {

        "temporary": 0.3,

        "workaround": 0.4,

        "rollback": 0.4,

        "hotfix": 0.3,

        "crash": 0.5,

        "urgent": 0.2
    }

    semantic_score = 0

    detected_patterns = []

    for word, weight in risk_keywords.items():

        if word in commit_message.lower():

            semantic_score += weight

            detected_patterns.append(word)

    semantic_score = min(
        semantic_score,
        1.0
    )

    return {

        "semantic_score": semantic_score,

        "patterns": detected_patterns
    }