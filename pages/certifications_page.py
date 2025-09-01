import streamlit as st

st.title("🎓 My Certifications")

st.divider()

st.subheader(":material/code: Google Crash Course on Python")
with st.expander("View Certificate"):
    st.image("images/PythonBeginnerCourse.jpeg")

st.divider()

st.subheader(":material/cloud_done: AWS Cloud Practitioner")
with st.expander("View Certificate"):

    st.image("images/AWSCloudPractionerSS.png")

st.divider()

st.subheader(":material/code: Python For Data Science & AI")
with st.expander("View Certificate"):
    st.image("Images/PythonForDataScienece&AI.jpeg")
