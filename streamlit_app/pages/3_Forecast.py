import streamlit as st
import plotly.express as px
import pandas as pd
import joblib
from pathlib import Path

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

# ==========================================
# LIVE DEMAND PREDICTION
# ==========================================

st.subheader("🤖 Live Demand Prediction")

st.caption(
    "Select a store, SKU and forecast date. "
    "Historical demand features are automatically retrieved."
)

# ------------------------------------------
# LOAD FORECAST DATASET
# ------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]

FORECAST_PATH = (
    BASE_DIR.parent
    / "data"
    / "processed"
    / "forecast_dataset.csv"
)

ENCODER_PATH = (
    BASE_DIR.parent
    / "models"
    / "encoders.pkl"
)

try:
    forecast_df = pd.read_csv(FORECAST_PATH)
    forecast_df["date"] = pd.to_datetime(forecast_df["date"])

    encoders = joblib.load(ENCODER_PATH)

except Exception as e:
    st.error(f"❌ Forecast resources could not be loaded: {e}")
    st.stop()


# ------------------------------------------
# INPUT SECTION
# ------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    store_options = sorted(
        forecast_df["store_id"].astype(str).unique()
    )

    selected_store = st.selectbox(
        "🏪 Store",
        store_options
    )


with col2:

    sku_options = sorted(
        forecast_df[
            forecast_df["store_id"].astype(str) == selected_store
        ]["sku_id"]
        .astype(str)
        .unique()
    )

    selected_sku = st.selectbox(
        "📦 SKU",
        sku_options
    )


with col3:

    date_options = sorted(
        forecast_df[
            (forecast_df["store_id"].astype(str) == selected_store)
            &
            (forecast_df["sku_id"].astype(str) == selected_sku)
        ]["date"]
        .dt.date
        .unique()
    )

    if len(date_options) == 0:
        st.warning("⚠️ No historical data found for this Store + SKU.")
        st.stop()

    selected_date = st.selectbox(
        "📅 Forecast Date",
        date_options
    )


# ------------------------------------------
# FIND HISTORICAL ROW
# ------------------------------------------

matching_rows = forecast_df[
    (forecast_df["store_id"].astype(str) == selected_store)
    &
    (forecast_df["sku_id"].astype(str) == selected_sku)
    &
    (forecast_df["date"].dt.date == selected_date)
]


if matching_rows.empty:

    st.warning(
        "⚠️ No matching historical record found for the selected inputs."
    )

else:

    row = matching_rows.iloc[0]

    st.markdown("---")

    # --------------------------------------
    # BUSINESS INPUTS
    # --------------------------------------

    st.subheader("📋 Forecast Inputs")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        unit_price = st.number_input(
            "💰 Unit Price",
            min_value=0.0,
            value=float(row["unit_price"]),
            step=1.0
        )

    with col2:

        discount_pct = st.number_input(
            "🏷️ Discount %",
            min_value=0.0,
            max_value=100.0,
            value=float(row["discount_pct"]),
            step=1.0
        )

    with col3:

        stock_on_hand = st.number_input(
            "📦 Stock On Hand",
            min_value=0,
            value=int(row["stock_on_hand"]),
            step=1
        )

    with col4:

        reorder_point = st.number_input(
            "🔄 Reorder Point",
            min_value=0,
            value=int(row["reorder_point"]),
            step=1
        )


    col1, col2 = st.columns(2)

    with col1:

        safety_stock = st.number_input(
            "🛡️ Safety Stock",
            min_value=0,
            value=int(row["safety_stock"]),
            step=1
        )

    with col2:

        st.metric(
            "📊 Automatically Calculated Stock Gap",
            f"{stock_on_hand - reorder_point}"
        )


    # --------------------------------------
    # AUTOMATIC FEATURES
    # --------------------------------------

    year = int(row["year"])
    month = int(row["month"])
    week = int(row["week"])
    day = int(row["day"])
    day_of_week = int(row["day_of_week"])
    is_weekend = int(row["is_weekend"])

    lag_1 = float(row["lag_1"])
    lag_7 = float(row["lag_7"])
    lag_30 = float(row["lag_30"])

    rolling_7 = float(row["rolling_7"])
    rolling_30 = float(row["rolling_30"])

    stock_gap = float(stock_on_hand - reorder_point)


    # --------------------------------------
    # SHOW AUTOMATIC FEATURES
    # --------------------------------------

    with st.expander("🔍 View Automatically Generated Features"):

        feature_col1, feature_col2, feature_col3 = st.columns(3)

        with feature_col1:

            st.metric("Lag 1", f"{lag_1:.2f}")
            st.metric("Lag 7", f"{lag_7:.2f}")
            st.metric("Lag 30", f"{lag_30:.2f}")

        with feature_col2:

            st.metric("Rolling 7", f"{rolling_7:.2f}")
            st.metric("Rolling 30", f"{rolling_30:.2f}")
            st.metric("Stock Gap", f"{stock_gap:.2f}")

        with feature_col3:

            st.metric("Year", year)
            st.metric("Month", month)
            st.metric("Week", week)


    st.markdown("---")


    # --------------------------------------
    # PREDICTION
    # --------------------------------------

    if st.button(
        "🚀 Predict Demand",
        use_container_width=True
    ):

        try:

            # Encode categorical values
            encoded_store = int(
                encoders["store_id"]
                .transform([str(selected_store)])[0]
            )

            encoded_sku = int(
                encoders["sku_id"]
                .transform([str(selected_sku)])[0]
            )

            encoded_category = int(
                encoders["category"]
                .transform([str(row["category"])])[0]
            )

            encoded_channel = int(
                encoders["channel"]
                .transform([str(row["channel"])])[0]
            )


            # ----------------------------------
            # API PAYLOAD
            # ----------------------------------

            payload = {

                "store_id": encoded_store,

                "sku_id": encoded_sku,

                "category": encoded_category,

                "channel": encoded_channel,

                "unit_price": float(unit_price),

                "discount_pct": float(discount_pct),

                "stock_on_hand": int(stock_on_hand),

                "reorder_point": int(reorder_point),

                "safety_stock": int(safety_stock),

                "year": year,

                "month": month,

                "week": week,

                "day": day,

                "day_of_week": day_of_week,

                "is_weekend": is_weekend,

                "lag_1": lag_1,

                "lag_7": lag_7,

                "lag_30": lag_30,

                "rolling_7": rolling_7,

                "rolling_30": rolling_30,

                "stock_gap": stock_gap
            }


            # ----------------------------------
            # CALL FASTAPI
            # ----------------------------------

            result = get_prediction(payload)


            # ----------------------------------
            # DISPLAY RESULT
            # ----------------------------------

            if "Predicted_Demand" in result:

                prediction = result["Predicted_Demand"]

                st.success(
                    f"✅ Predicted Demand: {prediction:.2f} units"
                )

                st.metric(
                    "📈 Forecasted Demand",
                    f"{prediction:.2f}"
                )

            else:

                st.error(
                    f"❌ Prediction Error: {result.get('error', 'Unknown error')}"
                )

        except Exception as e:

            st.error(
                f"❌ Prediction failed: {e}"
            )


st.markdown("---")

st.caption(
    "© 2026 Project FORESIGHT | Demand Forecast Dashboard"
)