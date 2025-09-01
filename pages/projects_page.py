import streamlit as st

st.title("💼 My Projects")

st.divider()

# --- Project Section ---
st.header("🗂️ The Portfolio")
st.write("""
A simple, elegant web portfolio to showcase my certifications, projects, and contact info.

**Built with:** Python, Streamlit, Custom design
""")
st.markdown("[🔗 View on GitHub](https://github.com/ayush-java/portfolio)")
st.divider()

# --- TarkAI Project Section ---
st.header("🗂️ TarkAI")
st.write("""
TarkAI helps students quickly understand long PDF company reports using AI. I led the team and we won 2nd place in HackAI, a company-sponsored hackathon by LTI Mindtree.

Our tool processes annual report PDFs, finds key parts like risks and financials, and explains them in simple words. As a prize, we also earned an interview opportunity with LTI Mindtree.

**Built with**: Python, Streamlit, and teamwork.
""")
with st.expander("View Demo Video"):
    st.video("https://www.youtube.com/watch?v=ULDonbj5Z2w&t=5s")
st.markdown("[🔗 View on GitHub](https://github.com/ayush-java/TarkAI-2025)")
st.divider()
