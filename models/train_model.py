import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
import joblib

df = pd.read_csv('data/processed_commits.csv')

X = df[[
    'loc',
    'complexity',
    'churn',
    'commit_frequency',
    'developer_experience',
    'files_modified',
    'risk_density',
    'complexity_ratio',
    'activity_score'
]]

y = df['defect']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

lr = LogisticRegression()

model = VotingClassifier(
    estimators=[
        ('rf', rf),
        ('lr', lr)
    ],
    voting='soft'
)

model.fit(X_train, y_train)

joblib.dump(
    model,
    'models/saved_model.pkl'
)

print("Model trained successfully.")