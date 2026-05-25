import os
import json
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
# Get project root directory
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

# Reports folder path
reports_dir = os.path.join(
    BASE_DIR,
    "reports"
)

# Create reports folder if missing
os.makedirs(
    reports_dir,
    exist_ok=True
)

# JSON output path
json_path = os.path.join(
    reports_dir,
    "latest_prediction.json"
)

# Save latest prediction
with open(json_path, "w") as f:

    json.dump(result, f, indent=4)

print("\nPrediction JSON updated successfully.")