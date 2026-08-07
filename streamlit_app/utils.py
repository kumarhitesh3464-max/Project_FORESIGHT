import pandas as pd
import streamlit as st
from pathlib import Path

# ==========================================
# BASE DIRECTORY
# ==========================================

BASE_DIR = Path(__file__).parent

DATA_PATH = (
    BASE_DIR.parent
    / "data"
    / "processed"
    / "risk_scored_dataset.csv"
)

# ==========================================
# LOAD DATA
# ==========================================

@st.cache_data
def load_data():

    try:

        df = pd.read_csv(DATA_PATH)

        # Remove duplicates
        df = df.drop_duplicates()

        # Clean column names
        df.columns = df.columns.str.strip()

        return df

    except FileNotFoundError:

        st.error("❌ Dataset not found.")

        st.stop()

    except Exception as e:

        st.error(f"❌ Error Loading Dataset : {e}")

        st.stop()