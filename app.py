
import streamlit as st


# Page configuration
st.set_page_config(
    page_title="Page Turners",
    page_icon="📚",
    layout="wide"
)

# Define navigation pages
pages = [
    st.Page(
        "home.py",
        title="Home",
        icon=":material/home:",
        default=True
    ),
    st.Page(
        "pages/1_Popularity.py",
        title="Popularity & Ratings",
        icon=":material/trending_up:"
    ),
    st.Page(
        "pages/2_Publication_Years.py",
        title="Publication Years",
        icon=":material/calendar_month:"
    ),
    st.Page(
        "pages/3_Literary_Genres.py",
        title="Literary Genres",
        icon=":material/menu_book:"
    ),
    st.Page(
        "pages/4_Ratings_Distribution.py",
        title="Ratings Distribution",
        icon=":material/star:"
    )
]

# Display selected page
navigation = st.navigation(pages)
navigation.run()
