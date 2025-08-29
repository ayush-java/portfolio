import streamlit as st

home_page = st.Page("pages/home_page.py", title="About Me!", icon="👋")
certifications_page = st.Page("pages/certifications_page.py", title="Certifications", icon="🎓")
projects_page = st.Page("pages/projects_page.py", title="Projects", icon="💼")


pages = {
    "Home": [home_page],
    "Achievements": [certifications_page],
    "Projects": [projects_page]
}