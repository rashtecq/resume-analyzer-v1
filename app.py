import streamlit as st
from resume_parser import extract_text
from analyzer import analyze

st.set_page_config(page_title="Resume Analyzer AI")
st.title("📄 Resume Analyzer & Skill Gap Advisor")

resume_file = st.file_uploader(
    "Upload your Resume (PDF/DOCX)",
    type=["pdf", "docx"]
)

job_desc = st.text_area("Paste Job Description")

if resume_file and job_desc:
    with st.spinner("Analyzing..."):
        resume_text = extract_text(resume_file)
        result = analyze(resume_text, job_desc)

    st.subheader("🔍 Analysis Result")
    st.write(result)
