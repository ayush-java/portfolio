import streamlit as st

home_page = st.Page("pages/home_page.py", title="About Me!", icon="👋")
certifications_page = st.Page("pages/certifications_page.py", title="Certifications", icon="🎓")
projects_page = st.Page("pages/projects_page.py", title="Projects", icon="💼")
myNexus_page = st.Page("pages/nexus_page.py", title="My Nexus", icon="🛠️")
myResume_page = st.Page("pages/resume_page.py", title="My Resume", icon="📄")
experience_page = st.Page("pages/experience_page.py", title="Experience", icon="🚀")

pages = {
    "Home": [home_page],
    "Achievements": [certifications_page],
    "Resume": [myResume_page],
    "Projects": [projects_page],
    "Experience": [experience_page],
    "Interests": [myNexus_page]
}