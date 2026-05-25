import joblib
import pandas as pd
from llm.llm_analysis import analyze_commit

model = joblib.load(
    'models/saved_model.pkl'
)

def predict_defect(
    loc,
    complexity,
    churn,
    commit_frequency,
    developer_experience,
    files_modified,
    commit_message
):

    risk_density = churn / loc

    complexity_ratio = (
        complexity / files_modified
    )

    activity_score = (
        commit_frequency *
        files_modified
    )

    features = pd.DataFrame([{
        "loc": loc,
        "complexity": complexity,
        "churn": churn,
        "commit_frequency": commit_frequency,
        "developer_experience": developer_experience,
        "files_modified": files_modified,
        "risk_density": risk_density,
        "complexity_ratio": complexity_ratio,
        "activity_score": activity_score
    }])

    ml_probability = (
        model.predict_proba(features)[0][1]
    )

    # LLM analysis
    llm_result = analyze_commit(
        commit_message
    )

    semantic_score = (
    llm_result["semantic_risk_score"]
    )
    
    # Hybrid score
    final_score = (
        0.7 * ml_probability +
        0.3 * semantic_score
    )

    quality_gate = (
        "FAILED"
        if final_score > 0.7
        else "PASSED"
    )

    return {
        "ml_probability": round(float(ml_probability), 2),
        "semantic_score": semantic_score,
        "final_score": round(float(final_score), 2),
        "quality_gate": quality_gate,
        "llm_analysis": llm_result
    }