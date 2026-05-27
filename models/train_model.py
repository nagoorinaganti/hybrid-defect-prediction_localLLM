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

    f1_score,

    confusion_matrix,

    classification_report
)

import joblib
from sklearn.metrics import roc_curve, auc

import matplotlib.pyplot as plt


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

print("\n========== CROSS VALIDATION ==========\n")

print(scores)

print("\nAverage Accuracy:")

print(scores.mean())

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

accuracy = accuracy_score(
    y_test,
    y_pred
)

precision = precision_score(
    y_test,
    y_pred
)

recall = recall_score(
    y_test,
    y_pred
)

f1 = f1_score(
    y_test,
    y_pred
)

print("\n========== MODEL EVALUATION ==========\n")

print(f"Accuracy : {accuracy:.2f}")

print(f"Precision: {precision:.2f}")

print(f"Recall   : {recall:.2f}")

print(f"F1 Score : {f1:.2f}")

# Confusion Matrix
cm = confusion_matrix(
    y_test,
    y_pred
)

print("\n========== CONFUSION MATRIX ==========\n")

print(cm)

# ROC Curve
y_probs = model.predict_proba(X_test)[:,1]

fpr, tpr, thresholds = roc_curve(
    y_test,
    y_probs
)

roc_auc = auc(fpr, tpr)

plt.figure()

plt.plot(
    fpr,
    tpr,
    label=f"AUC = {roc_auc:.2f}"
)

plt.plot([0,1],[0,1],'--')

plt.xlabel("False Positive Rate")

plt.ylabel("True Positive Rate")

plt.title("ROC Curve")

plt.legend()

plt.savefig(
    "reports/roc_curve.png"
)

print("\nROC Curve generated.")

joblib.dump(

    model,

    'saved_model.pkl'
)

print(
    "\nModel trained successfully."
)