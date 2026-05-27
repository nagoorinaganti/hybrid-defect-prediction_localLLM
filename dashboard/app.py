import streamlit as st
import json
import os

st.set_page_config(
    page_title="Hybrid Defect Prediction Dashboard",
    layout="wide"
)

st.title(
    "Hybrid ML + Semantic Risk Dashboard"
)


# ------------------------------------------------
# JSON Path
# ------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

json_path = os.path.join(
    BASE_DIR,
    "reports",
    "latest_prediction.json"
)


# ------------------------------------------------
# Load Results
# ------------------------------------------------

with open(json_path) as f:

    result = json.load(f)


# ------------------------------------------------
# Display Scores
# ------------------------------------------------

st.subheader("Prediction Scores")

st.write(
    f"ML Probability: {result['ml_probability']}"
)

st.write(
    f"Semantic Score: {result['semantic_score']}"
)

st.write(
    f"Final Hybrid Score: {result['final_score']}"
)

st.write(
    f"Quality Gate: {result['quality_gate']}"
)


# ------------------------------------------------
# Features
# ------------------------------------------------

st.subheader(
    "Extracted Software Engineering Metrics"
)

st.json(result["features"])