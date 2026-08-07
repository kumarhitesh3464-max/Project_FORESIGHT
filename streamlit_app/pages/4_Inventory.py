import streamlit as st
import plotly.express as px

from utils import load_data
from sidebar import sidebar_filters

st.set_page_config(
    page_title="Inventory Dashboard",
    page_icon="📦",
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

st.title("📦 Inventory Dashboard")

st.caption("Monitor inventory levels, reorder points, safety stock and inventory gaps.")

st.markdown("---")

# ==========================================
# KPI SECTION
# ==========================================

st.subheader("📌 Inventory Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📦 Avg Inventory",
        f"{filtered_df['Stock_On_Hand'].mean():.2f}"
    )

with col2:
    st.metric(
        "🔄 Avg Reorder Point",
        f"{filtered_df['Reorder_Point'].mean():.2f}"
    )

with col3:
    st.metric(
        "🛡 Avg Safety Stock",
        f"{filtered_df['Safety_Stock'].mean():.2f}"
    )

with col4:
    st.metric(
        "⚠ Avg Inventory Gap",
        f"{filtered_df['Inventory_Gap'].mean():.2f}"
    )

st.markdown("---")

# ==========================================
# INVENTORY CHARTS
# ==========================================

left, right = st.columns(2)

with left:

    fig = px.histogram(
        filtered_df,
        x="Stock_On_Hand",
        nbins=30,
        title="Inventory Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    gap = (
        filtered_df
        .groupby("store_id", as_index=False)["Inventory_Gap"]
        .mean()
    )

    fig = px.bar(
        gap,
        x="store_id",
        y="Inventory_Gap",
        color="Inventory_Gap",
        title="Inventory Gap by Store"
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

compare = (
    filtered_df
    .groupby("store_id", as_index=False)[
        ["Reorder_Point", "Safety_Stock"]
    ]
    .mean()
)

fig = px.line(
    compare,
    x="store_id",
    y=["Reorder_Point", "Safety_Stock"],
    markers=True,
    title="Reorder Point vs Safety Stock"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================
# INVENTORY TABLE
# ==========================================

st.subheader("📋 Inventory Details")

inventory = filtered_df[
    [
        "store_id",
        "sku_id",
        "Stock_On_Hand",
        "Reorder_Point",
        "Safety_Stock",
        "Inventory_Gap"
    ]
]

st.dataframe(
    inventory.head(100),
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# ==========================================
# DOWNLOAD
# ==========================================

st.subheader("⬇ Download Inventory Report")

csv = inventory.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Inventory CSV",
    data=csv,
    file_name="inventory_report.csv",
    mime="text/csv"
)

st.markdown("---")

# ==========================================
# EXECUTIVE INSIGHTS
# ==========================================

st.subheader("📊 Inventory Insights")

col1, col2 = st.columns(2)

with col1:

    st.success(f"""
**Highest Inventory Store:** {filtered_df.groupby('store_id')['Stock_On_Hand'].sum().idxmax()}

**Highest Reorder Point:** {filtered_df['Reorder_Point'].max():.2f}
""")

with col2:

    st.info(f"""
**Average Inventory Gap:** {filtered_df['Inventory_Gap'].mean():.2f}

**Highest Safety Stock:** {filtered_df['Safety_Stock'].max():.2f}
""")

st.markdown("---")

st.caption("© 2026 Project FORESIGHT | Inventory Dashboard")