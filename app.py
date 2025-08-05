import streamlit as st
import pandas as pd
from utils import parser, analyzer, exporter
import json
import os

st.set_page_config(page_title="Document Compliance Checker", layout="wide")

st.title("📄 AI-Powered Document Compliance Checker")

# Upload file
uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "xlsx", "eml", "msg"])
checklist_files = [f for f in os.listdir("checklists") if f.endswith(".json")]

# Checklist selection
if checklist_files:
    checklist_name = st.selectbox("Select a checklist", checklist_files)
else:
    st.warning("No checklist files found in /checklists")
    checklist_name = None

if uploaded_file and checklist_name:
    # Save file
    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Parse text
    text = parser.extract_text(file_path)

    # Load checklist
    with open(os.path.join("checklists", checklist_name), "r") as f:
        checklist = json.load(f)

    # Analyze
    results = analyzer.run_analysis(text, checklist)

    # Display results
    df = pd.DataFrame(results)
    st.dataframe(df, use_container_width=True)

    # Export buttons
    col1, col2 = st.columns(2)
    with col1:
        csv_data = exporter.to_csv(df)
        st.download_button("Download CSV", csv_data, "results.csv", "text/csv")
    with col2:
        excel_data = exporter.to_excel(df)
        st.download_button("Download Excel", excel_data, "results.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
