import streamlit as st
from openai import OpenAI

def generate_cover_letter(job_description):
    api_key = st.secrets.get("OPENAI_API_KEY") or None
    
    if not api_key:
        st.error("OpenAI API key not found. Please set OPENAI_API_KEY in your Streamlit secrets.")
        return None
    
    client = OpenAI(api_key=api_key)

    prompt = f'''
    Generate a professional offshore cover letter for Jason Bent.
    Highlight Stage 4 rigging, IRATA L2, hydraulic bolting and FPSO experience.

    Job Description:
    {job_description}
    '''

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content