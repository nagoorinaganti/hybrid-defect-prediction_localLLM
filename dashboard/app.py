import streamlit as st
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Hybrid ML + LLM Dashboard",
    layout="wide"
)

# Title
st.title(
    "Hybrid ML + LLM Defect Prediction Dashboard"
)

# Metrics Row
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Defect Probability",
        "87%"
    )

with col2:
    st.metric(
        "Semantic Risk Score",
        "0.65"
    )

with col3:
    st.metric(
        "Quality Gate",
        "FAILED"
    )

# Warning alert
st.warning(
    "High-risk commit detected during CI/CD execution."
)

# Risk Patterns
st.subheader("Detected Risk Patterns")

st.write([
    "temporary",
    "workaround",
    "crash"
])

# Accuracy Comparison Graph
st.subheader("Model Accuracy Comparison")

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

ax.set_ylabel("Accuracy (%)")

ax.set_title(
    "Accuracy Comparison"
)

st.pyplot(fig)

# Defect Escape Rate
st.subheader("Defect Escape Rate Reduction")

labels = [
    "Traditional CI/CD",
    "Hybrid Framework"
]

values = [
    18.6,
    8.7
]

fig2, ax2 = plt.subplots()

ax2.bar(labels, values)

ax2.set_ylabel(
    "Defect Escape Rate (%)"
)

ax2.set_title(
    "Defect Escape Rate Reduction"
)

st.pyplot(fig2)

# Pipeline Status
st.subheader("CI/CD Pipeline Status")

st.success(
    "Pipeline execution completed successfully."
)

# Footer
st.markdown("---")

st.caption(
    "BITS WILP Dissertation Prototype"
)