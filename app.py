
import streamlit as st


# Page configuration
st.set_page_config(
    page_title="Page Turners",
    page_icon="📚",
    layout="wide"
)

# Define navigation pages
pages = [
    st.Page("home.py", title="Home", icon="🏠", default=True),
    st.Page("pages/1_Popularity.py", title="Popularity & Ratings"),
    st.Page("pages/2_Publication_Years.py", title="Publication Years"),
    st.Page("pages/3_Literary_Genres.py", title="Literary Genres"),
    st.Page("pages/4_Ratings_Distribution.py", title="Ratings Distribution")
]

# Display selected page
navigation = st.navigation(pages)
navigation.run()
