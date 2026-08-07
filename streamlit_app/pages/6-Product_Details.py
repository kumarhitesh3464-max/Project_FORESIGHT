import streamlit as st
import plotly.express as px

from utils import load_data

st.set_page_config(
    page_title="Product Details",
    page_icon="🔍",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

df = load_data()

# ==========================================
# HEADER
# ==========================================

st.title("🔍 Product Details Dashboard")

st.caption("Analyze individual product performance, inventory and demand forecast.")

st.markdown("---")

# ==========================================
# PRODUCT SELECTION
# ==========================================

sku = st.selectbox(
    "📦 Select Product (SKU)",
    sorted(df["sku_id"].unique())
)

product = df[df["sku_id"] == sku]

st.markdown("---")

# ==========================================
# KPI SECTION
# ==========================================

st.subheader("📌 Product Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📈 Forecast",
        f"{product['Predicted'].mean():.2f}"
    )

with col2:
    st.metric(
        "📊 Actual Sales",
        f"{product['Actual'].mean():.2f}"
    )

with col3:
    st.metric(
        "📦 Inventory",
        f"{product['Stock_On_Hand'].mean():.2f}"
    )

with col4:
    st.metric(
        "⚠ Risk Score",
        f"{product['Risk_Score'].mean():.2f}"
    )

st.markdown("---")

# ==========================================
# FORECAST VS ACTUAL
# ==========================================

st.subheader("📈 Forecast vs Actual")

chart = product.copy()

chart["Record"] = range(1, len(chart) + 1)

fig = px.line(
    chart,
    x="Record",
    y=["Actual", "Predicted"],
    markers=True,
    title=f"Forecast Comparison - {sku}"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# INVENTORY STATUS
# ==========================================

st.subheader("📦 Inventory Status")

left, right = st.columns(2)

with left:

    fig = px.bar(
        product,
        x="store_id",
        y="Stock_On_Hand",
        color="Stock_On_Hand",
        title="Inventory by Store"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    fig = px.bar(
        product,
        x="store_id",
        y="Risk_Score",
        color="Risk_Score",
        title="Risk Score by Store"
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================
# PRODUCT INFORMATION
# ==========================================

st.subheader("📋 Product Details")

st.dataframe(
    product,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# ==========================================
# EXECUTIVE INSIGHTS
# ==========================================

st.subheader("📊 Product Insights")

col1, col2 = st.columns(2)

with col1:

    st.success(f"""
**Category:** {product['category'].iloc[0]}

**Channel:** {product['channel'].iloc[0]}
""")

with col2:

    st.info(f"""
**Average Forecast:** {product['Predicted'].mean():.2f}

**Average Risk:** {product['Risk_Score'].mean():.2f}
""")

st.markdown("---")

st.caption("© 2026 Project FORESIGHT | Product Details Dashboard")