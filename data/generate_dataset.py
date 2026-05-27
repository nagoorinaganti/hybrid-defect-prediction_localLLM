import pandas as pd
import random

data = []

for i in range(12000):

    loc = random.randint(10, 500)

    complexity = random.randint(1, 40)

    churn = random.randint(1, 150)

    commit_frequency = random.randint(1, 30)

    developer_activity = random.randint(1, 100)

    files_modified = random.randint(1, 10)

    historical_defects = random.randint(0, 5)

    risk_probability = min(

        (
            complexity * 0.015 +
            churn * 0.008 +
            files_modified * 0.05 +
            loc * 0.0005 +
            historical_defects * 0.1
        ),

        0.95
    )

    defect = 1 if random.random() < risk_probability else 0

    data.append([

        loc,

        complexity,

        churn,

        commit_frequency,

        developer_activity,

        files_modified,

        historical_defects,

        defect
    ])

df = pd.DataFrame(

    data,

    columns=[

        'loc',

        'complexity',

        'churn',

        'commit_frequency',

        'developer_activity',

        'files_modified',

        'historical_defects',

        'defect'
    ]
)

df.to_csv(

    'data/commits.csv',

    index=False
)

print(
    "Dataset generated successfully."
)