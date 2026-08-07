import streamlit as st
import plotly.express as px

from utils import load_data
from sidebar import sidebar_filters

st.set_page_config(
    page_title="Risk Dashboard",
    page_icon="⚠️",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

df = load_data()
filtered_df = sidebar_filters(df)

# ==========================================
# HEADER
# ==========================================

st.title("⚠️ Inventory Risk Dashboard")

st.caption("Monitor inventory risks and identify critical products across stores.")

st.markdown("---")

# ==========================================
# KPI SECTION
# ==========================================

st.subheader("📌 Risk Overview")

critical = (filtered_df["Risk_Level"] == "Critical").sum()
high = (filtered_df["Risk_Level"] == "High").sum()
medium = (filtered_df["Risk_Level"] == "Medium").sum()
low = (filtered_df["Risk_Level"] == "Low").sum()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🚨 Critical", critical)

with col2:
    st.metric("🔴 High", high)

with col3:
    st.metric("🟠 Medium", medium)

with col4:
    st.metric("🟢 Low", low)

st.markdown("---")

# ==========================================
# RISK CHARTS
# ==========================================

risk = (
    filtered_df["Risk_Level"]
    .value_counts()
    .reset_index()
)

risk.columns = ["Risk_Level", "Count"]

left, right = st.columns(2)

with left:

    fig = px.bar(
        risk,
        x="Risk_Level",
        y="Count",
        color="Risk_Level",
        title="Risk Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    fig = px.pie(
        risk,
        names="Risk_Level",
        values="Count",
        hole=0.45,
        title="Risk Share"
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================
# TOP RISK PRODUCTS
# ==========================================

st.subheader("🚨 Top 25 High Risk Products")

top_risk = (
    filtered_df
    .sort_values("Risk_Score", ascending=False)
    [
        [
            "store_id",
            "sku_id",
            "category",
            "Risk_Score",
            "Risk_Level"
        ]
    ]
)

st.dataframe(
    top_risk.head(25),
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# ==========================================
# CATEGORY & STORE RISK
# ==========================================

left, right = st.columns(2)

with left:

    category = (
        filtered_df
        .groupby("category", as_index=False)["Risk_Score"]
        .mean()
    )

    fig = px.bar(
        category,
        x="category",
        y="Risk_Score",
        color="Risk_Score",
        title="Average Risk by Category"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    store = (
        filtered_df
        .groupby("store_id", as_index=False)["Risk_Score"]
        .mean()
    )

    fig = px.bar(
        store,
        x="store_id",
        y="Risk_Score",
        color="Risk_Score",
        title="Average Risk by Store"
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================
# EXECUTIVE INSIGHTS
# ==========================================

st.subheader("📊 Risk Insights")

col1, col2 = st.columns(2)

with col1:

    st.error(f"""
**Highest Risk Store:** {filtered_df.groupby('store_id')['Risk_Score'].mean().idxmax()}

**Highest Risk Category:** {filtered_df.groupby('category')['Risk_Score'].mean().idxmax()}
""")

with col2:

    st.warning(f"""
**Average Risk Score:** {filtered_df['Risk_Score'].mean():.2f}

**Maximum Risk Score:** {filtered_df['Risk_Score'].max():.2f}
""")

st.markdown("---")

st.caption("© 2026 Project FORESIGHT | Risk Dashboard")