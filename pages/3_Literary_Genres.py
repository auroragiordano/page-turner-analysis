
import streamlit as st

from src.streamlit_data import load_cached_data
from src.analysis import genre_analysis
from src.plots import plot_genres


# Load datasets
books = load_cached_data("books.csv")
book_tags = load_cached_data("book_tags.csv")
tags = load_cached_data("tags.csv")

genre_results = genre_analysis(books, book_tags, tags)


# Page introduction
st.markdown("""
<div style="text-align:center; padding:45px 10px 35px;">
    <p style="color:#6E6E73; font-size:13px; font-weight:600;">
        03 / LITERARY GENRES
    </p>
    <h1 style="font-size:54px; letter-spacing:-1.5px;
               color:#1D1D1F; line-height:1.15;">
        Every genre has a story.
    </h1>
    <p style="font-size:19px; color:#6E6E73;">
        Discovering which literary categories receive
        the highest average ratings.
    </p>
</div>
""", unsafe_allow_html=True)


# Select number of genres
top_n = st.selectbox(
    "Number of genres to display",
    options=[3, 5, 9],
    index=2
)

selected_genres = genre_results.head(top_n)


# Key statistics
col1, col2 = st.columns(2, gap="medium")

with col1:
    with st.container(border=True):
        st.metric(
            "Highest-Rated Category",
            genre_results.iloc[0]["tag_name"].title()
        )
        st.caption("Among the selected literary categories")

with col2:
    with st.container(border=True):
        st.metric(
            "Highest Average Rating",
            f"{genre_results.iloc[0]['average_rating']:.3f}"
        )
        st.caption("Average rating on a 1–5 scale")


st.write("")


# Main chart
with st.container(border=True):
    st.subheader("Average Book Rating by Genre")

    fig = plot_genres(selected_genres)
    st.pyplot(fig, use_container_width=True)

    st.caption(
        "Books can belong to multiple literary categories. "
        "Each book contributes equally to its category's average."
    )


st.write("")


# Key insight
with st.container(border=True):
    st.markdown("**KEY INSIGHT**")

    st.subheader("A little magic goes a long way.")

    st.write(
        f"Displaying the top {top_n} literary categories. "
        "Fantasy has the highest average rating among the "
        "nine selected categories, although differences "
        "between genres are relatively small."
    )
