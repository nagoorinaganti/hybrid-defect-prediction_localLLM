import pandas as pd

from sklearn.model_selection import (
    train_test_split,
    cross_val_score
)

from sklearn.ensemble import RandomForestClassifier

from sklearn.linear_model import LogisticRegression

from sklearn.ensemble import VotingClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

import joblib


df = pd.read_csv(
    'data/commits.csv'
)

X = df[

    [

        'loc',

        'complexity',

        'churn',

        'commit_frequency',

        'developer_activity',

        'files_modified',

        'historical_defects'
    ]
]

y = df['defect']


X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,
    test_size=0.2,
    random_state=42
)


rf = RandomForestClassifier()

lr = LogisticRegression(max_iter=1000)


model = VotingClassifier(

    estimators=[

        ('rf', rf),

        ('lr', lr)
    ],

    voting='soft'
)


model.fit(X_train, y_train)


scores = cross_val_score(

    model,
    X,
    y,
    cv=5
)

print("\nCross Validation Scores:")

print(scores)

print("\nAverage Accuracy:")

print(scores.mean())


y_pred = model.predict(X_test)

print("\nAccuracy:")

print(
    accuracy_score(y_test, y_pred)
)

print("\nPrecision:")

print(
    precision_score(y_test, y_pred)
)

print("\nRecall:")

print(
    recall_score(y_test, y_pred)
)

print("\nF1 Score:")

print(
    f1_score(y_test, y_pred)
)


joblib.dump(

    model,

    'saved_model.pkl'
)

print(
    "\nModel trained successfully."
)