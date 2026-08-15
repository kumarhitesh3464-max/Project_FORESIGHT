import streamlit as st
from pathlib import Path
from PIL import Image

# ==========================================
# BASE DIRECTORY
# ==========================================

BASE_DIR = Path(__file__).parent

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Project FORESIGHT – AI-Powered Demand & Inventory Intelligence Platform",
    page_icon=str(BASE_DIR / "assets" / "favicon.png"),
    layout="wide"
)


# ==========================================
# LOAD CSS
# ==========================================

with open(BASE_DIR / "style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ==========================================
# IMPORT MODULES
# ==========================================

from utils import load_data
from sidebar import sidebar_filters
from kpi import show_kpis

from charts import (

    # SALES
    monthly_sales,
    sales_store_analysis,
    sales_category_analysis,
    sales_channel_analysis,

    # FORECAST
    forecast_distribution,
    forecast_vs_actual,
    monthly_forecast,
    weekly_forecast,
    sku_forecast,

    # INVENTORY
    inventory_distribution,
    inventory_gap,
    reorder_vs_safety,

    # RISK
    risk_distribution,
    stock_status,
    category_risk,
    store_risk

)

from tables import (
    top_risk_products,
    top_forecast_products,
    dataset_preview
)

# ==========================================
# LOAD IMAGES
# ==========================================

banner = Image.open(BASE_DIR / "assets" / "banner.png")
logo = Image.open(BASE_DIR / "assets" / "logo.png")

# ==========================================
# LOAD DATA
# ==========================================

df = load_data()

# ==========================================
# SIDEBAR FILTERS
# ==========================================

filtered_df = sidebar_filters(df)

# ==========================================
# HEADER
# ==========================================

st.image(
    banner,
    use_container_width=True
)

st.image(
    logo,
    width=180
)

st.markdown("""

# 📦 PROJECT FORESIGHT

###Project FORESIGHT – AI-Powered Demand & Inventory Intelligence Platform

**Predict Today • Optimize Tomorrow**

""")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("📈 Demand Forecasting")

with col2:
    st.info("📦 Inventory Optimization")

with col3:
    st.error("⚠ Risk Detection")

st.markdown("---")

# ==========================================
# KPI CARDS
# ==========================================

show_kpis(filtered_df)

st.markdown("---")

# ==========================================
# SALES ANALYTICS
# ==========================================

monthly_sales(filtered_df)

st.markdown("---")

sales_store_analysis(filtered_df)

st.markdown("---")

sales_category_analysis(filtered_df)

st.markdown("---")

sales_channel_analysis(filtered_df)

st.markdown("---")

# ==========================================
# FORECAST
# ==========================================

forecast_vs_actual(filtered_df)

st.markdown("---")

forecast_distribution(filtered_df)

st.markdown("---")

monthly_forecast(filtered_df)

st.markdown("---")

weekly_forecast(filtered_df)

st.markdown("---")

sku_forecast(filtered_df)

st.markdown("---")

# ==========================================
# INVENTORY
# ==========================================

inventory_distribution(filtered_df)

st.markdown("---")

inventory_gap(filtered_df)

st.markdown("---")

reorder_vs_safety(filtered_df)

st.markdown("---")

# ==========================================
# RISK
# ==========================================

risk_distribution(filtered_df)

st.markdown("---")

stock_status(filtered_df)

st.markdown("---")

category_risk(filtered_df)

st.markdown("---")

store_risk(filtered_df)

st.markdown("---")

# ==========================================
# TABLES
# ==========================================

top_risk_products(filtered_df)

st.markdown("---")

top_forecast_products(filtered_df)

st.markdown("---")

dataset_preview(filtered_df.head(100))

st.markdown("---")

# ==========================================
# DOWNLOAD
# ==========================================

st.subheader("⬇ Download Filtered Dataset")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="filtered_inventory_data.csv",
    mime="text/csv"
)

st.markdown("---")

# ==========================================
# EXECUTIVE INSIGHTS
# ==========================================

st.subheader("📊 Executive Insights")

col1, col2 = st.columns(2)

with col1:

    st.info(f"""

**Highest Forecast Store:** {filtered_df.groupby('store_id')['Predicted'].sum().idxmax()}

**Highest Demand Month:** {filtered_df.groupby('month')['Predicted'].sum().idxmax()}

**Highest Risk Category:** {filtered_df.groupby('category')['Risk_Score'].mean().idxmax()}

""")

with col2:

    st.success(f"""

**Average Inventory Gap:** {filtered_df['Inventory_Gap'].mean():.2f}

**Critical Products:** {(filtered_df['Risk_Level']=='Critical').sum()}

**Average Forecast:** {filtered_df['Predicted'].mean():.2f}

""")

st.markdown("---")

st.caption(
    "© 2026 Project FORESIGHT – AI-Powered Demand & Inventory Intelligence Platform"
)