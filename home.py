
import streamlit as st


# Page configuration
st.set_page_config(
    page_title="Page Turners",
    page_icon="📚",
    layout="wide"
)

# Project introduction
st.title("📚 Page Turners")
st.subheader("Exploring Goodreads Books and Ratings")

st.write(
    "An interactive dashboard exploring book popularity, "
    "average ratings, publication years, and literary genres "
    "using the Goodreads dataset."
)

st.divider()

# Dataset overview
st.header("Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Books", "10,000")

with col2:
    st.metric("User Ratings", "5,976,479")

with col3:
    st.metric("Unique Tags", "34,252")

st.divider()

# Project objectives
st.header("Project Objectives")

st.write("""
1. Are the most popular books also the highest-rated?
2. Do average ratings differ across publication decades?
3. Which literary genres receive the highest average ratings?
4. How are user ratings distributed from 1 to 5 stars?
""")

st.info("Select a page from the sidebar to explore the analyses.")
