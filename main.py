import json
import os

from models.predict import predict_defect

from utils.feature_extraction import *


# ------------------------------------------------
# Extract commit message
# ------------------------------------------------

commit_message = get_latest_commit_message()


# ------------------------------------------------
# Extract Git metrics
# ------------------------------------------------

git_metrics = get_git_diff_metrics()


# ------------------------------------------------
# Complexity
# ------------------------------------------------

complexity = get_complexity("main.py")


# ------------------------------------------------
# Commit Frequency
# ------------------------------------------------

commit_frequency = get_commit_frequency()


# ------------------------------------------------
# Developer Activity
# ------------------------------------------------

developer_activity = get_developer_activity()


# ------------------------------------------------
# Historical defect indicators
# ------------------------------------------------

historical_defects = get_historical_defects(
    commit_message
)


# ------------------------------------------------
# Prediction
# ------------------------------------------------

result = predict_defect(

    loc=git_metrics["loc"],

    complexity=complexity,

    churn=git_metrics["churn"],

    commit_frequency=commit_frequency,

    developer_activity=developer_activity,

    files_modified=git_metrics["files_modified"],

    historical_defects=historical_defects,

    commit_message=commit_message
)


print("\n========== FINAL RESULT ==========\n")

print(result)


# ------------------------------------------------
# Save prediction
# ------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

reports_dir = os.path.join(
    BASE_DIR,
    "reports"
)

os.makedirs(
    reports_dir,
    exist_ok=True
)

json_path = os.path.join(
    reports_dir,
    "latest_prediction.json"
)

with open(json_path, "w") as f:

    json.dump(result, f, indent=4)

print(
    "\nPrediction JSON updated successfully."
)