import streamlit as st
import matplotlib.pyplot as plt

st.title(
    "Hybrid ML + LLM Quality Dashboard"
)

st.metric(
    "Final Defect Risk",
    "87%"
)

st.metric(
    "Quality Gate",
    "FAILED"
)

st.warning(
    "High-risk commit detected"
)

models = [
    "Logistic Regression",
    "Random Forest",
    "Hybrid ML + LLM"
]

accuracy = [
    78.4,
    86.7,
    91.2
]

fig, ax = plt.subplots()

ax.bar(models, accuracy)

ax.set_ylabel("Accuracy")

st.pyplot(fig)