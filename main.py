from models.predict import predict_defect
from utils.git_utils import (
    get_latest_commit_message
)

# Get real latest commit message
commit_message = get_latest_commit_message()

print("\n========== LATEST COMMIT ==========\n")

print(commit_message)

# Run prediction
result = predict_defect(
    loc=180,
    complexity=22,
    churn=55,
    commit_frequency=14,
    developer_experience=5,
    files_modified=4,
    commit_message=commit_message
)

print("\n========== FINAL RESULT ==========\n")

print(result)