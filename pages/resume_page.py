import streamlit as st
import os
import base64

st.title("📄 My Resume")
st.divider()

resume_path = os.path.join("static", "Ayush_Velhal_Resume.pdf")

# Download button
with open(resume_path, "rb") as f:
    st.download_button(
        label="Download Resume (PDF)",
        data=f,
        file_name="Ayush_Velhal_Resume.pdf",
        mime="application/pdf"
    )