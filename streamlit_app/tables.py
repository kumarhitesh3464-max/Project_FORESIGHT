import streamlit as st

# ==========================================
# TOP RISK PRODUCTS
# ==========================================

def top_risk_products(df):

    st.subheader("🚨 Top 10 High Risk Products")

    risk_df = (
        df.sort_values("Risk_Score", ascending=False)
        [
            [
                "store_id",
                "sku_id",
                "category",
                "Risk_Score",
                "Risk_Level"
            ]
        ]
        .head(10)
    )

    st.dataframe(
        risk_df,
        use_container_width=True,
        hide_index=True
    )


# ==========================================
# TOP FORECAST PRODUCTS
# ==========================================

def top_forecast_products(df):

    st.subheader("📈 Top 10 Forecast Products")

    forecast_df = (
        df.sort_values("Predicted", ascending=False)
        [
            [
                "store_id",
                "sku_id",
                "category",
                "Predicted"
            ]
        ]
        .head(10)
    )

    st.dataframe(
        forecast_df,
        use_container_width=True,
        hide_index=True
    )


# ==========================================
# TOP SALES PRODUCTS
# ==========================================

def top_sales_products(df):

    st.subheader("💰 Top 10 Sales Products")

    sales_df = (
        df.sort_values("Actual", ascending=False)
        [
            [
                "store_id",
                "sku_id",
                "category",
                "Actual"
            ]
        ]
        .head(10)
    )

    st.dataframe(
        sales_df,
        use_container_width=True,
        hide_index=True
    )


# ==========================================
# INVENTORY TABLE
# ==========================================

def inventory_table(df):

    st.subheader("📦 Inventory Details")

    inventory = df[
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


# ==========================================
# PRODUCT DETAILS TABLE
# ==========================================

def product_details(df):

    st.subheader("🔍 Product Details")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


# ==========================================
# DATASET PREVIEW
# ==========================================

def dataset_preview(df):

    st.subheader("📋 Dataset Preview")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


# ==========================================
# DOWNLOAD TABLE
# ==========================================

def download_table(df, filename):

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download CSV",
        data=csv,
        file_name=filename,
        mime="text/csv"
    )