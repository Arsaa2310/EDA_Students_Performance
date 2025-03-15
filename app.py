import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("Student_performance_data _.csv")
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filter Data")
selected_gender = st.sidebar.multiselect("Pilih Gender:", df["Gender"].unique(), default=df["Gender"].unique())
selected_ethnicity = st.sidebar.multiselect("Pilih Ethnicity:", df["Ethnicity"].unique(), default=df["Ethnicity"].unique())
selected_parent_edu = st.sidebar.multiselect("Pilih Parental Education:", df["ParentalEducation"].unique(), default=df["ParentalEducation"].unique())

df_filtered = df[df["Gender"].isin(selected_gender) & df["Ethnicity"].isin(selected_ethnicity) & df["ParentalEducation"].isin(selected_parent_edu)]

# Dashboard Title
st.title("📊 Student Performance Dashboard")
st.write("Analisis performa siswa berdasarkan berbagai faktor.")

# Display Data
st.subheader("📌 Data Overview")
st.dataframe(df_filtered)

# Visualizations
st.subheader("📈 Distribusi GPA Siswa")
fig, ax = plt.subplots(figsize=(8,5))
sns.histplot(df_filtered["GPA"], kde=True, color="blue", label="GPA", ax=ax)
plt.legend()
st.pyplot(fig)

# Correlation Heatmap
st.subheader("🔍 Korelasi Antar Variabel")
fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(df_filtered[["GPA", "StudyTimeWeekly", "Absences"]].corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Additional Insights
st.subheader("📊 Aktivitas Ekstrakurikuler dan GPA")
fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(x="Extracurricular", y="GPA", data=df_filtered, ax=ax)
st.pyplot(fig)

st.write("💡 *Gunakan filter di sidebar untuk menganalisis data lebih mendalam.*")
