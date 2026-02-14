import streamlit as st
from matcher import score_job
from generator import generate_cover_letter

st.title("Jason Bent Offshore Application Agent")

job_description = st.text_area("Paste Job Description Here")

if st.button("Analyze Job"):
    score, category = score_job(job_description)
    st.write(f"Match Score: {score}%")
    st.write(f"Category: {category}")

    cover_letter = generate_cover_letter(job_description)
    st.subheader("Generated Cover Letter")
    st.write(cover_letter)