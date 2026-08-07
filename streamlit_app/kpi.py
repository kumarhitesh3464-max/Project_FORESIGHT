import streamlit as st

# ==========================================
# KPI CARDS
# ==========================================

def show_kpis(df):

    total_products = len(df)

    avg_forecast = round(df["Predicted"].mean(), 2)

    avg_risk = round(df["Risk_Score"].mean(), 2)

    avg_inventory = round(df["Stock_On_Hand"].mean(), 2)

    critical_products = (df["Risk_Level"] == "Critical").sum()

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            label="📦 Total Products",
            value=f"{total_products:,}",
            delta="Inventory"
        )

    with col2:
        st.metric(
            label="📈 Avg Forecast",
            value=f"{avg_forecast:,.2f}",
            delta="Demand"
        )

    with col3:
        st.metric(
            label="⚠️ Avg Risk Score",
            value=f"{avg_risk:,.2f}",
            delta="Risk"
        )

    with col4:
        st.metric(
            label="🏪 Avg Inventory",
            value=f"{avg_inventory:,.2f}",
            delta="Stock"
        )

    with col5:
        st.metric(
            label="🚨 Critical Products",
            value=f"{critical_products:,}",
            delta="Attention"
        )