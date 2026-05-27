import joblib
import pandas as pd
from llm.llm_analysis import analyze_commit


model = joblib.load(
    'saved_model.pkl'
)


def predict_defect(

    loc,

    complexity,

    churn,

    commit_frequency,

    developer_activity,

    files_modified,

    historical_defects,

    commit_message
):

    features = pd.DataFrame([{

    "loc": loc,

    "complexity": complexity,

    "churn": churn,

    "commit_frequency": commit_frequency,

    "developer_activity": developer_activity,

    "files_modified": files_modified,

    "historical_defects": historical_defects
}])

    ml_probability = model.predict_proba(
        features
    )[0][1]

    llm_result = analyze_commit(
        commit_message
    )

    semantic_score = llm_result[
        "semantic_score"
    ]

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

        "ml_probability": round(
            ml_probability,
            2
        ),

        "semantic_score": semantic_score,

        "final_score": round(
            final_score,
            2
        ),

        "quality_gate": quality_gate,

        "features": {

            "loc": loc,

            "complexity": complexity,

            "churn": churn,

            "commit_frequency": commit_frequency,

            "developer_activity": developer_activity,

            "files_modified": files_modified,

            "historical_defects": historical_defects
        }
    }