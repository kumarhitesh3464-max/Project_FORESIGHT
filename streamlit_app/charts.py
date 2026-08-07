import streamlit as st
import plotly.express as px

# ==========================================
# Monthly Sales Trend
# ==========================================

def monthly_sales(df):

    st.subheader("📈 Monthly Sales Trend")

    monthly = (
        df.groupby("month", as_index=False)["Actual"]
        .sum()
        .sort_values("month")
    )

    fig = px.line(
        monthly,
        x="month",
        y="Actual",
        markers=True,
        title="Monthly Sales"
    )

    st.plotly_chart(fig, use_container_width=True)
    # ==========================================
# Store Sales
# ==========================================

def sales_store_analysis(df):

    st.subheader("🏪 Store Sales")

    store = (
        df.groupby("store_id", as_index=False)["Actual"]
        .sum()
        .sort_values("Actual", ascending=False)
    )

    fig = px.bar(
        store,
        x="store_id",
        y="Actual",
        color="Actual",
        title="Store Sales"
    )

    st.plotly_chart(fig, use_container_width=True)
    # ==========================================
# Category Sales
# ==========================================

def sales_category_analysis(df):

    st.subheader("📦 Category Sales")

    category = (
        df.groupby("category", as_index=False)["Actual"]
        .sum()
        .sort_values("Actual", ascending=False)
    )

    fig = px.bar(
        category,
        x="category",
        y="Actual",
        color="Actual",
        title="Category Sales"
    )

    st.plotly_chart(fig, use_container_width=True)
    # ==========================================
# Channel Sales
# ==========================================

def sales_channel_analysis(df):

    st.subheader("🛒 Channel Sales")

    channel = (
        df.groupby("channel", as_index=False)["Actual"]
        .sum()
    )

    fig = px.pie(
        channel,
        names="channel",
        values="Actual",
        hole=0.45,
        title="Sales by Channel"
    )

    st.plotly_chart(fig, use_container_width=True)
    # ==========================================
# Forecast Distribution
# ==========================================

def forecast_distribution(df):

    st.subheader("📈 Forecast Distribution")

    fig = px.histogram(
        df,
        x="Predicted",
        nbins=30,
        title="Forecast Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)
    # ==========================================
# Monthly Forecast
# ==========================================

def monthly_forecast(df):

    st.subheader("📅 Monthly Forecast")

    monthly = (
        df.groupby("month", as_index=False)["Predicted"]
        .sum()
        .sort_values("month")
    )

    fig = px.line(
        monthly,
        x="month",
        y="Predicted",
        markers=True,
        title="Monthly Forecast"
    )

    st.plotly_chart(fig, use_container_width=True)
    # ==========================================
# Weekly Forecast
# ==========================================

def weekly_forecast(df):

    st.subheader("📆 Weekly Forecast")

    weekly = (
        df.groupby("week", as_index=False)["Predicted"]
        .sum()
        .sort_values("week")
    )

    fig = px.line(
        weekly,
        x="week",
        y="Predicted",
        markers=True,
        title="Weekly Forecast"
    )

    st.plotly_chart(fig, use_container_width=True)
    # ==========================================
# SKU Forecast
# ==========================================

def sku_forecast(df):

    st.subheader("📦 Top Forecasted Products")

    sku = (
        df.groupby("sku_id", as_index=False)["Predicted"]
        .sum()
        .sort_values("Predicted", ascending=False)
        .head(10)
    )

    fig = px.bar(
        sku,
        x="sku_id",
        y="Predicted",
        color="Predicted",
        title="Top Forecasted SKUs"
    )

    st.plotly_chart(fig, use_container_width=True)
    # ==========================================
# Inventory Distribution
# ==========================================

def inventory_distribution(df):

    st.subheader("📦 Inventory Distribution")

    fig = px.histogram(
        df,
        x="Stock_On_Hand",
        nbins=30,
        title="Inventory Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    # ==========================================
# Inventory Gap
# ==========================================

def inventory_gap(df):

    st.subheader("📉 Inventory Gap by Store")

    gap = (
        df
        .groupby("store_id", as_index=False)["Inventory_Gap"]
        .mean()
    )

    fig = px.bar(
        gap,
        x="store_id",
        y="Inventory_Gap",
        color="Inventory_Gap",
        title="Average Inventory Gap"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    # ==========================================
# Reorder Point vs Safety Stock
# ==========================================

def reorder_vs_safety(df):

    st.subheader("📦 Reorder Point vs Safety Stock")

    compare = (
        df
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

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    # ==========================================
# Risk Distribution
# ==========================================

def risk_distribution(df):

    st.subheader("⚠ Risk Distribution")

    risk = (
        df["Risk_Level"]
        .value_counts()
        .reset_index()
    )

    risk.columns = ["Risk_Level", "Count"]

    fig = px.bar(
        risk,
        x="Risk_Level",
        y="Count",
        color="Risk_Level",
        title="Risk Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    # ==========================================
# Stock Status
# ==========================================

def stock_status(df):

    st.subheader("📦 Stock Status")

    stock = (
        df["Risk_Level"]
        .value_counts()
        .reset_index()
    )

    stock.columns = ["Risk_Level", "Count"]

    fig = px.pie(
        stock,
        names="Risk_Level",
        values="Count",
        hole=0.45,
        title="Stock Status"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    # ==========================================
# Category Risk
# ==========================================

def category_risk(df):

    st.subheader("📦 Average Risk by Category")

    category = (
        df
        .groupby("category", as_index=False)["Risk_Score"]
        .mean()
    )

    fig = px.bar(
        category,
        x="category",
        y="Risk_Score",
        color="Risk_Score",
        title="Category Risk"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    # ==========================================
# Store Risk
# ==========================================

def store_risk(df):

    st.subheader("🏪 Store Risk")

    store = (
        df
        .groupby("store_id", as_index=False)["Risk_Score"]
        .mean()
    )

    fig = px.bar(
        store,
        x="store_id",
        y="Risk_Score",
        color="Risk_Score",
        title="Store Risk Score"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    # ==========================================
# Forecast vs Actual
# ==========================================

def forecast_vs_actual(df):

    st.subheader("📈 Forecast vs Actual")

    compare = (
        df.groupby("month", as_index=False)[
            ["Actual", "Predicted"]
        ]
        .sum()
        .sort_values("month")
    )

    fig = px.line(
        compare,
        x="month",
        y=["Actual", "Predicted"],
        markers=True,
        title="Forecast vs Actual Sales"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    # ==========================================
# Product Forecast
# ==========================================

def product_forecast(df):

    st.subheader("📈 Product Forecast")

    fig = px.line(
        df,
        x="date",
        y="Predicted",
        color="store_id",
        title="Forecast Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    # ==========================================
# Product Inventory
# ==========================================

def product_inventory(df):

    st.subheader("📦 Product Inventory")

    fig = px.bar(
        df,
        x="store_id",
        y="Stock_On_Hand",
        color="Stock_On_Hand",
        title="Inventory by Store"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    # ==========================================
# Executive Risk Chart
# ==========================================

def executive_risk_chart(df):

    st.subheader("⚠ Executive Risk Summary")

    risk = (
        df["Risk_Level"]
        .value_counts()
        .reset_index()
    )

    risk.columns = ["Risk_Level", "Count"]

    fig = px.pie(
        risk,
        names="Risk_Level",
        values="Count",
        hole=0.5,
        title="Overall Business Risk"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    # ==========================================
# Forecast Accuracy
# ==========================================

def forecast_accuracy(df):

    st.subheader("🎯 Forecast Accuracy")

    compare = (
        df.groupby("month", as_index=False)[
            ["Actual", "Predicted"]
        ]
        .sum()
    )

    fig = px.bar(
        compare,
        x="month",
        y=["Actual", "Predicted"],
        barmode="group",
        title="Forecast Accuracy"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    # ==========================================
# Business KPI Chart
# ==========================================

def business_kpi(df):

    st.subheader("📊 Business KPI")

    kpi = {
        "Metric": [
            "Forecast",
            "Inventory",
            "Risk"
        ],
        "Value": [
            df["Predicted"].mean(),
            df["Stock_On_Hand"].mean(),
            df["Risk_Score"].mean()
        ]
    }

    fig = px.bar(
        kpi,
        x="Metric",
        y="Value",
        color="Metric",
        title="Business KPI"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    