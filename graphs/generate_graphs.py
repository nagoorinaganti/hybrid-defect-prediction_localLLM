import matplotlib.pyplot as plt

models = [

    "Logistic Regression",

    "Random Forest",

    "Hybrid ML + LLM"
]

accuracy = [78, 87, 91]

plt.figure()

plt.bar(models, accuracy)

plt.ylabel("Accuracy")

plt.title("Model Accuracy Comparison")

plt.savefig(
    "reports/accuracy_comparison.png"
)

print(
    "Accuracy graph generated."
)