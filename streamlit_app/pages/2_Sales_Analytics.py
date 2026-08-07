import streamlit as st

from utils import load_data
from sidebar import sidebar_filters
from charts import (
    sales_store_analysis,
    sales_category_analysis,
    sales_channel_analysis
)

st.set_page_config(
    page_title="Sales Analytics",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

df = load_data()

filtered_df = sidebar_filters(df)

# ==========================================
# PAGE HEADER
# ==========================================

st.title("📊 Sales Analytics Dashboard")

st.caption("Analyze sales performance across stores, categories and sales channels.")

st.markdown("---")

# ==========================================
# KPI SECTION
# ==========================================

st.subheader("📌 Sales Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Total Sales",
        f"{filtered_df['Actual'].sum():,.0f}"
    )

with col2:
    st.metric(
        "📈 Average Sales",
        f"{filtered_df['Actual'].mean():.2f}"
    )

with col3:
    st.metric(
        "🏪 Stores",
        filtered_df["store_id"].nunique()
    )

with col4:
    st.metric(
        "📦 Products",
        filtered_df["sku_id"].nunique()
    )

st.markdown("---")

# ==========================================
# SALES CHARTS
# ==========================================

left, right = st.columns(2)

with left:
    sales_store_analysis(filtered_df)

with right:
   sales_category_analysis(filtered_df)

st.markdown("---")

sales_channel_analysis(filtered_df)

st.markdown("---")

# ==========================================
# TOP PRODUCTS
# ==========================================

st.subheader("🏆 Top 20 Best Selling Products")

top_products = (
    filtered_df
    .sort_values("Actual", ascending=False)
    [["sku_id", "store_id", "category", "Actual"]]
    .head(20)
)

st.dataframe(
    top_products,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# ==========================================
# BUSINESS INSIGHTS
# ==========================================

st.subheader("📋 Sales Insights")

col1, col2 = st.columns(2)

with col1:

    st.success(f"""
**Top Store:** {filtered_df.groupby('store_id')['Actual'].sum().idxmax()}

**Top Category:** {filtered_df.groupby('category')['Actual'].sum().idxmax()}
""")

with col2:

    st.info(f"""
**Top Sales Channel:** {filtered_df.groupby('channel')['Actual'].sum().idxmax()}

**Highest Sales:** {filtered_df['Actual'].max():,.2f}
""")

st.markdown("---")

st.caption("© 2026 Project FORESIGHT | Sales Analytics")