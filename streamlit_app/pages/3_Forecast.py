import streamlit as st
import plotly.express as px
from utils import load_data
from sidebar import sidebar_filters
from api import get_prediction

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
st.markdown("---")

st.subheader("🤖 Live Demand Prediction (FastAPI)")

col1, col2 = st.columns(2)

with col1:

    store_id = st.number_input("Store ID", value=1)

    sku_id = st.number_input("SKU ID", value=101)

    category = st.number_input("Category", value=1)

    channel = st.number_input("Channel", value=1)

    unit_price = st.number_input("Unit Price", value=500.0)

    discount_pct = st.number_input("Discount %", value=10.0)

    stock_on_hand = st.number_input("Stock On Hand", value=200)

    reorder_point = st.number_input("Reorder Point", value=50)

    safety_stock = st.number_input("Safety Stock", value=30)

with col2:

    year = st.number_input("Year", value=2026)

    month = st.number_input("Month", value=8)

    week = st.number_input("Week", value=31)

    day = st.number_input("Day", value=7)

    day_of_week = st.number_input("Day of Week", value=5)

    is_weekend = st.number_input("Weekend (0/1)", value=0)

    lag_1 = st.number_input("Lag 1", value=120.0)

    lag_7 = st.number_input("Lag 7", value=118.0)

    lag_30 = st.number_input("Lag 30", value=115.0)

    rolling_7 = st.number_input("Rolling 7", value=119.0)

    rolling_30 = st.number_input("Rolling 30", value=117.0)

    stock_gap = st.number_input("Stock Gap", value=150.0)


if st.button("🚀 Predict Demand"):

    payload = {
        "store_id": int(store_id),
        "sku_id": int(sku_id),
        "category": int(category),
        "channel": int(channel),
        "unit_price": float(unit_price),
        "discount_pct": float(discount_pct),
        "stock_on_hand": int(stock_on_hand),
        "reorder_point": int(reorder_point),
        "safety_stock": int(safety_stock),
        "year": int(year),
        "month": int(month),
        "week": int(week),
        "day": int(day),
        "day_of_week": int(day_of_week),
        "is_weekend": int(is_weekend),
        "lag_1": float(lag_1),
        "lag_7": float(lag_7),
        "lag_30": float(lag_30),
        "rolling_7": float(rolling_7),
        "rolling_30": float(rolling_30),
        "stock_gap": float(stock_gap)
    }

    result = get_prediction(payload)

    if "Predicted_Demand" in result:

        st.success(
            f"✅ Predicted Demand : {result['Predicted_Demand']:.2f}"
        )

    else:

        st.error(result["error"])

st.caption("© 2026 Project FORESIGHT | Demand Forecast Dashboard")