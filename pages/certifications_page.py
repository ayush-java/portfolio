import streamlit as st

st.title("🎓 My Certifications")

st.divider()

st.subheader(":material/code: Google Crash Course on Python")
st.write("I successfully completed the ‘Crash Course on Python’ by Google on Coursera on August 30, 2024. This course helped me strengthen my understanding of Python fundamentals, data structures, and problem-solving skills. It marks an important step in building my programming foundation and growing my technical abilities.")
with st.expander("View Certificate"):
    st.image("images/PythonBeginnerCourse.jpeg")

st.divider()

st.subheader(":material/cloud_done: AWS Cloud Practitioner")
st.write("I successfully completed the AWS Cloud Practitioner Essentials training on August 3, 2025. This course gave me a strong understanding of core AWS services, global infrastructure, security, pricing, and cloud fundamentals. It marks my first step into cloud computing and strengthens my foundation to pursue advanced AWS certifications and projects.")
with st.expander("View Certificate"):
    st.image("images/AWSCloudPractionerSS.png")

st.divider()

st.subheader(":material/code: Python For Data Science & AI")
st.write("I successfully completed the Python for Data Science and AI course by IBM on August 31, 2025. This program gave me hands-on experience with Python libraries like Pandas, NumPy, and Matplotlib, while also introducing machine learning and AI applications. It strengthened my skills in applying Python to real-world data science problems and building AI-driven solutions.")
with st.expander("View Certificate"):
    st.image("Images/PythonForDataScienece&AI.jpeg")
