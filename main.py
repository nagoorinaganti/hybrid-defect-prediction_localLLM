from models.predict import predict_defect

result = predict_defect(
    loc=180,
    complexity=22,
    churn=55,
    commit_frequency=14,
    developer_experience=5,
    files_modified=4,
    commit_message=(
        "Temporary workaround added "
        "for memory crash issue"
    )
)

print("\n========== FINAL RESULT ==========\n")

print(result)