from pathlib import Path
from PIL import Image
import streamlit as st

# ==========================================
# SIDEBAR FILTERS
# ==========================================
BASE_DIR = Path(__file__).parent

logo = Image.open(BASE_DIR / "assets" / "logo.png")

st.sidebar.image(
    logo,
    width=170
)
def sidebar_filters(df):

    st.sidebar.markdown("## 📦 Project FORESIGHT")
    st.sidebar.caption("Retail Demand Forecasting")

    st.sidebar.markdown("---")

    st.sidebar.subheader("🎛 Dashboard Filters")

    # -----------------------------
    # Store Filter
    # -----------------------------
    store = st.sidebar.multiselect(
        "🏪 Select Store",
        sorted(df["store_id"].unique()),
        default=sorted(df["store_id"].unique())
    )

    # -----------------------------
    # Category Filter
    # -----------------------------
    category = st.sidebar.multiselect(
        "📦 Select Category",
        sorted(df["category"].unique()),
        default=sorted(df["category"].unique())
    )

    # -----------------------------
    # Channel Filter
    # -----------------------------
    channel = st.sidebar.multiselect(
        "🛒 Select Channel",
        sorted(df["channel"].unique()),
        default=sorted(df["channel"].unique())
    )

    # -----------------------------
    # Risk Filter
    # -----------------------------
    risk = st.sidebar.multiselect(
        "⚠ Select Risk Level",
        sorted(df["Risk_Level"].unique()),
        default=sorted(df["Risk_Level"].unique())
    )

    # -----------------------------
    # Apply Filters
    # -----------------------------
    filtered_df = df[
        (df["store_id"].isin(store)) &
        (df["category"].isin(category)) &
        (df["channel"].isin(channel)) &
        (df["Risk_Level"].isin(risk))
    ]
    st.sidebar.markdown("---")
    st.sidebar.caption("Version 1.0")
    st.sidebar.caption("© 2026 Project FORESIGHT")
    return filtered_df