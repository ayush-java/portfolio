import streamlit as st

st.title("👋 About Me!")

st.divider()

# Reduce image size to half using width argument
st.image("images/portrait.jpg", width=350)

st.write("""
I’m a CS student at UT Dallas focused on AI/ML and Cloud. This portfolio highlights my projects, certifications, and an easy way to contact me.
""")

st.subheader("Tech I use often")

st.markdown(
    """
    <style>
        .badge {
            display: inline-block;
            background-color: #eee;
            color: #333;
            border-radius: 12px;
            padding: 6px 16px;
            margin-right: 8px;
            font-size: 16px;
            font-weight: 500;
            box-shadow: 0 1px 4px rgba(0,0,0,0.08);
        }
    </style>
    <div>
        <div class="badge">Python</div>
        <div class="badge">Java</div>
        <div class="badge">Streamlit</div>
        <div class="badge">React</div>
        <div class="badge">TensorFlow</div>
        <div class="badge">MediaPipe</div>
    </div>
    """,
    unsafe_allow_html=True
)
