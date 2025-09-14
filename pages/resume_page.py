import streamlit as st
import os
import base64

st.title("📄 My Resume")
st.divider()

resume_path = os.path.join("static", "LatestResume_AyushVelhal.pdf")

# Display PDF inline using an iframe
# with open(resume_path, "rb") as f:
#     base64_pdf = base64.b64encode(f.read()).decode("utf-8")
#     pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="900" type="application/pdf"></iframe>'
#     st.markdown(pdf_display, unsafe_allow_html=True)

# st.pdf("static/LatestResume_AyushVelhal.pdf", height=600)

# Download button
with open(resume_path, "rb") as f:
    st.download_button(
        label="Download Resume (PDF)",
        data=f,
        file_name="Resume_Sep2025.pdf",
        mime="application/pdf"
    )
