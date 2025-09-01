import streamlit as st

st.title("My Tech Nexus 🛠️")

st.write(
    "This is my Nexus of tools and technologies — the ones I enjoy working with, "
    "the reasons they stand out to me, and the ways I’ve brought them to life in real projects."
)

st.subheader(":material/code: Streamlit")
with st.expander("Why I Love Streamlit"):
    st.markdown(
        """
        Streamlit lets me build interactive web apps with pure Python—no front-end hassle! I used it to create this portfolio, organizing my projects, certifications, and contact info in a clean, dynamic layout.
        
        - **Easy UI:** Functions like `st.title()` and `st.write()` make adding headings and text simple.
        - **Interactive Elements:** Dropdowns (`st.selectbox`), text inputs (`st.text_input`), and buttons (`st.button`) add user-friendly interactivity.
        - **Seamless Integration:** Python logic connects directly to the UI, so I can filter results or show different content based on user choices.
        - **Professional Look:** Streamlit helps me design polished, lightweight sites that are easy to maintain.
        
        I love how Streamlit lets me mix text, visuals, and interactivity in a single flow. It's my go-to for building fast, beautiful apps!
        """
    )

st.subheader(":material/cloud_done: AWS Cloud")
with st.expander("Why I Like AWS Cloud"):
    st.markdown(
        """
        I started my AWS Cloud journey with the AWS Cloud Practitioner certification, which gave me a solid introduction to cloud computing. AWS stands out as one of the easiest and most reliable clouds to get started with.
        
        - **Beginner-Friendly:** Clear services like EC2 (servers), S3 (storage), and IAM (security) make it simple to use.
        - **Intuitive Console:** The AWS console is well-structured, so I can manage resources without feeling overwhelmed.
        - **Industry Adoption:** AWS is widely used, with many tools and resources available for all skill levels.
        - **Certification Insights:** I learned about cost management, scalability, and how companies use AWS to build at any size.
        
        Even at the foundational level, AWS has shown me how easy it is to start working with the cloud—and why it's the most trusted platform for future projects.
        """
    )
