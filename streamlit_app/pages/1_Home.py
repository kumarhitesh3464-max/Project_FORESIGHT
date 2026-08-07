import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

# ======================================
# HERO SECTION
# ======================================

st.title("🏠 PROJECT FORESIGHT")

st.markdown("""
### Retail Demand Forecasting & Inventory Risk Management System

### 🚀 Predict Today • Optimize Tomorrow
""")

st.markdown("---")

# ======================================
# QUICK OVERVIEW
# ======================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📦 Datasets", "4")

with col2:
    st.metric("🤖 ML Models", "6+")

with col3:
    st.metric("📊 Dashboards", "7")

with col4:
    st.metric("⚠ Risk Engine", "Enabled")

st.markdown("---")

# ======================================
# BUSINESS PROBLEM
# ======================================

st.header("📌 Business Problem")

st.write("""
Retail businesses frequently struggle with:

- ❌ Stock-outs
- ❌ Overstocking
- ❌ Poor Demand Forecasting
- ❌ High Inventory Holding Cost
- ❌ Revenue Loss

Project FORESIGHT provides an AI-powered inventory forecasting solution
to help businesses make better inventory decisions.
""")

st.markdown("---")

# ======================================
# PROJECT OBJECTIVES
# ======================================

st.header("🎯 Project Objectives")

c1, c2 = st.columns(2)

with c1:

    st.success("""
✅ Forecast Product Demand

✅ Optimize Inventory

✅ Improve Supply Planning
""")

with c2:

    st.info("""
✅ Detect Inventory Risk

✅ Reduce Holding Cost

✅ Support Business Decisions
""")

st.markdown("---")

# ======================================
# DATASETS
# ======================================

st.header("📂 Datasets")

dataset = {
    "Dataset": [
        "sales_daily.csv",
        "sku_master.csv",
        "calendar.csv",
        "inventory_snapshots.csv"
    ],
    "Purpose": [
        "Sales History",
        "Product Master",
        "Calendar Features",
        "Inventory Status"
    ]
}

st.dataframe(dataset, use_container_width=True)

st.markdown("---")

# ======================================
# PROJECT WORKFLOW
# ======================================

st.header("⚙ End-to-End Workflow")

st.write("""
1️⃣ Business Understanding

2️⃣ Data Collection

3️⃣ Data Cleaning

4️⃣ Exploratory Data Analysis

5️⃣ Feature Engineering

6️⃣ Machine Learning Forecasting

7️⃣ Model Evaluation

8️⃣ Inventory Risk Scoring

9️⃣ Professional Dashboard

🔟 Deployment

1️⃣1️⃣ Executive Summary
""")

st.markdown("---")

# ======================================
# TECH STACK
# ======================================

st.header("🛠 Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:

    st.info("""
### Programming

• Python

• Pandas

• NumPy

• Scikit-Learn
""")

with col2:

    st.info("""
### Machine Learning

• XGBoost

• Random Forest

• LightGBM

• Prophet
""")

with col3:

    st.info("""
### Visualization

• Streamlit

• Plotly

• GitHub

• VS Code
""")

st.markdown("---")

# ======================================
# PROJECT STATUS
# ======================================

st.success("✅ Project FORESIGHT Successfully Loaded")

st.caption("© 2026 Project FORESIGHT | Retail Demand Forecasting System")