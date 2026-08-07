import streamlit as st
import plotly.express as px

from utils import load_data

st.set_page_config(
    page_title="Executive Summary",
    page_icon="📋",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

df = load_data()

# ==========================================
# HEADER
# ==========================================

st.title("📋 Executive Summary Dashboard")

st.caption("Business Overview | Model Performance | Business Recommendations")

st.markdown("---")

# ==========================================
# EXECUTIVE KPI
# ==========================================

st.subheader("📌 Executive Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📦 Products",
        len(df)
    )

with col2:
    st.metric(
        "🏪 Stores",
        df["store_id"].nunique()
    )

with col3:
    st.metric(
        "📈 Avg Forecast",
        f"{df['Predicted'].mean():.2f}"
    )

with col4:
    st.metric(
        "⚠ Avg Risk",
        f"{df['Risk_Score'].mean():.2f}"
    )

st.markdown("---")

# ==========================================
# BUSINESS PROBLEM
# ==========================================

st.header("🏢 Business Problem")

st.write("""
Retail businesses frequently experience:

- Stock-outs
- Overstock Inventory
- Poor Demand Forecasting
- High Holding Cost
- Revenue Loss

Project FORESIGHT addresses these challenges using
Machine Learning based Demand Forecasting and Inventory Risk Scoring.
""")

st.markdown("---")

# ==========================================
# PROJECT ACHIEVEMENTS
# ==========================================

st.header("🏆 Project Achievements")

left, right = st.columns(2)

with left:

    st.success("""
✅ Demand Forecasting Model

✅ Inventory Risk Engine

✅ Professional Streamlit Dashboard

✅ Interactive Business Analytics
""")

with right:

    st.success("""
✅ Store Analysis

✅ Category Analysis

✅ Channel Analysis

✅ Executive Decision Support
""")

st.markdown("---")

# ==========================================
# MODEL PERFORMANCE
# ==========================================

st.header("🤖 Model Summary")

performance = {
    "Metric": [
        "Forecast Generated",
        "Risk Score Generated",
        "Inventory Gap",
        "Business Dashboard"
    ],
    "Status": [
        "Completed",
        "Completed",
        "Completed",
        "Completed"
    ]
}

st.dataframe(
    performance,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# ==========================================
# RISK DISTRIBUTION
# ==========================================

st.header("⚠ Overall Risk Distribution")

risk = (
    df["Risk_Level"]
    .value_counts()
    .reset_index()
)

risk.columns = ["Risk_Level", "Count"]

fig = px.pie(
    risk,
    names="Risk_Level",
    values="Count",
    hole=0.45,
    title="Overall Inventory Risk"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# BUSINESS RECOMMENDATIONS
# ==========================================

st.header("💡 Business Recommendations")

st.info("""
📈 Increase stock for high-demand products.

⚠ Monitor Critical Risk products daily.

📦 Optimize Reorder Point using forecasting.

🛡 Improve Safety Stock strategy.

💰 Reduce excess inventory to lower holding costs.

📊 Use Project FORESIGHT dashboard for decision making.
""")

st.markdown("---")

# ==========================================
# PROJECT OUTCOME
# ==========================================

st.header("🎯 Final Outcome")

st.write("""
Project FORESIGHT provides an end-to-end AI-driven Retail Demand Forecasting
and Inventory Risk Management solution.

The system enables organizations to:

- Improve Demand Planning
- Reduce Inventory Loss
- Increase Product Availability
- Optimize Working Capital
- Support Executive Decision Making
""")

st.markdown("---")

st.success("✅ Executive Summary Completed Successfully")

st.caption("© 2026 Project FORESIGHT | Executive Dashboard")