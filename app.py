import streamlit as st
import pandas as pd
import numpy as np
import requests
from dotenv import load_dotenv
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Optional AI libraries
from google import genai
from langchain_community.llms import Ollama

load_dotenv()

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Study Planner",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Study Planner")
st.write("Welcome to your smart study planning assistant!")

# -----------------------------
# Student Details
# -----------------------------
st.header("👩‍🎓 Student Details")

name = st.text_input("Enter your name")
course = st.text_input("Enter your course")

subjects = st.multiselect(
    "Select your subjects",
    [
        "Python",
        "Java",
        "DBMS",
        "Data Structures",
        "Probability & Statistics",
        "Artificial Intelligence"
    ]
)

hours = st.number_input(
    "Available study hours per day",
    min_value=1,
    max_value=12,
    value=3
)

# -----------------------------
# Study Plan
# -----------------------------
if st.button("Generate Study Plan"):

    if name and subjects:

        st.success(f"Study plan generated for {name}! 🎉")

        total_hours = hours
        hours_per_subject = round(total_hours / len(subjects), 2)

        data = []

        for subject in subjects:
            data.append({
                "Subject": subject,
                "Hours": hours_per_subject
            })

        df = pd.DataFrame(data)

        st.subheader("📅 Your Study Plan")
        st.dataframe(df, use_container_width=True)

        # -----------------------------
        # Chart
        # -----------------------------
        st.subheader("📊 Study Hours Distribution")

        fig, ax = plt.subplots()

        sns.barplot(
            data=df,
            x="Subject",
            y="Hours",
            ax=ax
        )

        plt.xticks(rotation=30)
        plt.tight_layout()

        st.pyplot(fig)

        # -----------------------------
        # Recommendation
        # -----------------------------
        st.subheader("💡 Recommendation")

        hardest_subject = subjects[0]

        st.info(
            f"Spend extra revision time on **{hardest_subject}** "
            "and practice important concepts regularly."
        )

    else:
        st.warning("Please enter your name and select at least one subject.")

# -----------------------------
# Student Data
# -----------------------------
st.sidebar.header("📋 Student Information")

st.sidebar.write("Name:", name if name else "Not entered")
st.sidebar.write("Course:", course if course else "Not entered")
st.sidebar.write("Daily Hours:", hours)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("🤖 AI Study Planner | Python + Streamlit")