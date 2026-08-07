import streamlit as st
import plotly.express as px

from utils import load_data
from sidebar import sidebar_filters

st.set_page_config(
    page_title="Forecast",
    page_icon="📈",
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

st.title("📈 Demand Forecast Dashboard")

st.caption("Analyze demand forecasts and compare predicted values with actual sales.")

st.markdown("---")

# ==========================================
# KPI SECTION
# ==========================================

st.subheader("📌 Forecast Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📈 Avg Forecast",
        f"{filtered_df['Predicted'].mean():.2f}"
    )

with col2:
    st.metric(
        "📊 Avg Actual",
        f"{filtered_df['Actual'].mean():.2f}"
    )

with col3:
    st.metric(
        "🚀 Max Forecast",
        f"{filtered_df['Predicted'].max():.2f}"
    )

with col4:
    st.metric(
        "📉 Min Forecast",
        f"{filtered_df['Predicted'].min():.2f}"
    )

st.markdown("---")

# ==========================================
# MONTHLY & WEEKLY FORECAST
# ==========================================

left, right = st.columns(2)

with left:

    monthly = (
        filtered_df
        .groupby("month", as_index=False)[["Actual", "Predicted"]]
        .sum()
    )

    fig = px.line(
        monthly,
        x="month",
        y=["Actual", "Predicted"],
        markers=True,
        title="Monthly Actual vs Forecast"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    weekly = (
        filtered_df
        .groupby("week", as_index=False)[["Actual", "Predicted"]]
        .sum()
    )

    fig = px.line(
        weekly,
        x="week",
        y=["Actual", "Predicted"],
        markers=True,
        title="Weekly Forecast Trend"
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================
# SKU FORECAST
# ==========================================

st.subheader("📦 Top Forecasted Products")

sku = (
    filtered_df
    .groupby("sku_id", as_index=False)["Predicted"]
    .sum()
    .sort_values("Predicted", ascending=False)
    .head(20)
)

fig = px.bar(
    sku,
    x="sku_id",
    y="Predicted",
    color="Predicted",
    title="Top 20 Forecasted SKUs"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================
# FORECAST TABLE
# ==========================================

st.subheader("📋 Forecast Results")

forecast = filtered_df[
    [
        "store_id",
        "sku_id",
        "Actual",
        "Predicted"
    ]
]

st.dataframe(
    forecast.head(100),
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# ==========================================
# EXECUTIVE INSIGHTS
# ==========================================

st.subheader("📊 Forecast Insights")

col1, col2 = st.columns(2)

with col1:

    st.success(f"""
**Highest Forecast SKU:** {filtered_df.groupby('sku_id')['Predicted'].sum().idxmax()}

**Highest Forecast Month:** {filtered_df.groupby('month')['Predicted'].sum().idxmax()}
""")

with col2:

    st.info(f"""
**Average Forecast:** {filtered_df['Predicted'].mean():.2f}

**Highest Predicted Demand:** {filtered_df['Predicted'].max():.2f}
""")

st.markdown("---")

st.caption("© 2026 Project FORESIGHT | Demand Forecast Dashboard")