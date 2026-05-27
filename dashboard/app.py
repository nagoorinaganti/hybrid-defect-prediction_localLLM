import streamlit as st

import json

import os

from streamlit_autorefresh import st_autorefresh


# ------------------------------------------------
# Page Config
# ------------------------------------------------

st.set_page_config(

    page_title="Hybrid Defect Prediction Dashboard",

    layout="wide"
)


# ------------------------------------------------
# Auto Refresh Every 5 Seconds
# ------------------------------------------------

st_autorefresh(

    interval=5000,

    key="dashboard_refresh"
)


# ------------------------------------------------
# Dashboard Title
# ------------------------------------------------

st.title(

    "Hybrid ML + Semantic Risk Dashboard"
)


# ------------------------------------------------
# JSON Path
# ------------------------------------------------

BASE_DIR = os.path.dirname(

    os.path.dirname(
        os.path.abspath(__file__)
    )
)

json_path = os.path.join(

    BASE_DIR,

    "reports",

    "latest_prediction.json"
)


# ------------------------------------------------
# Verify File Exists
# ------------------------------------------------

if not os.path.exists(json_path):

    st.error(

        "latest_prediction.json not found."
    )

    st.stop()


# ------------------------------------------------
# Load Latest JSON
# ------------------------------------------------

with open(json_path, "r") as f:

    result = json.load(f)


# ------------------------------------------------
# Prediction Results
# ------------------------------------------------

st.subheader(

    "Prediction Scores"
)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(

        "ML Probability",

        result["ml_probability"]
    )

with col2:

    st.metric(

        "Semantic Score",

        result["semantic_score"]
    )

with col3:

    st.metric(

        "Final Hybrid Score",

        result["final_score"]
    )


# ------------------------------------------------
# Quality Gate
# ------------------------------------------------

st.subheader(

    "Quality Gate Status"
)

if result["quality_gate"] == "FAILED":

    st.error(

        "HIGH RISK COMMIT DETECTED"
    )

else:

    st.success(

        "LOW RISK COMMIT"
    )


# ------------------------------------------------
# Extracted Features
# ------------------------------------------------

st.subheader(

    "Extracted Software Engineering Metrics"
)

st.json(

    result["features"]
)


# ------------------------------------------------
# ROC Curve
# ------------------------------------------------

roc_path = os.path.join(

    BASE_DIR,

    "reports",

    "roc_curve.png"
)

if os.path.exists(roc_path):

    st.subheader(

        "ROC Curve"
    )

    st.image(roc_path)


# ------------------------------------------------
# Accuracy Comparison Graph
# ------------------------------------------------

graph_path = os.path.join(

    BASE_DIR,

    "reports",

    "accuracy_comparison.png"
)

if os.path.exists(graph_path):

    st.subheader(

        "Accuracy Comparison"
    )

    st.image(graph_path)