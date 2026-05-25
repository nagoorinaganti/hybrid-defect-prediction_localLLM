import pandas as pd

df = pd.read_csv('../data/commits.csv')

# Derived features
df['risk_density'] = (
    df['churn'] / df['loc']
)

df['complexity_ratio'] = (
    df['complexity'] /
    df['files_modified']
)

df['activity_score'] = (
    df['commit_frequency'] *
    df['files_modified']
)

df.to_csv(
    '../data/processed_commits.csv',
    index=False
)

print("Feature engineering completed.")