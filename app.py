import streamlit as st
from pages.menu import pages

st.set_page_config(layout="wide")


with st.sidebar:
    st.subheader("Contact Me")
    st.markdown("[:material/mark_email_read: Email](mailto:ayush.velhal@gmail.com)")
    st.markdown("[:material/link: LinkedIn](https://www.linkedin.com/in/ayush-velhal/)")
# st.button("Click me")

st.navigation(pages).run()