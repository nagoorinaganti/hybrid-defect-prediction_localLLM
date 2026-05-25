from models.predict import predict_defect

from utils.git_utils import (
    get_latest_commit_message,
    get_git_metrics
)

import json

# Real commit message
commit_message = get_latest_commit_message()

# Real Git metrics
metrics = get_git_metrics()

print("\n========== COMMIT MESSAGE ==========\n")

print(commit_message)

print("\n========== GIT METRICS ==========\n")

print(metrics)

# Run prediction
result = predict_defect(
    loc=metrics["loc"],
    complexity=metrics["complexity"],
    churn=metrics["churn"],
    commit_frequency=metrics["commit_frequency"],
    developer_experience=metrics["developer_experience"],
    files_modified=metrics["files_modified"],
    commit_message=commit_message
)

print("\n========== FINAL RESULT ==========\n")

print(result)

# Save latest prediction
with open(
    "reports/latest_prediction.json",
    "w"
) as f:

    json.dump(result, f, indent=4)