
import streamlit as st

from src.streamlit_data import load_cached_data
from src.analysis import popularity_analysis
from src.plots import plot_popularity


# Load data and calculate correlation
books = load_cached_data("books.csv")
correlation = popularity_analysis(books)


# Page introduction
st.markdown("""
<div style="text-align:center; padding:45px 10px 35px;">
    <p style="color:#6E6E73; font-size:13px; font-weight:600;">
        01 / POPULARITY & RATINGS
    </p>
    <h1 style="font-size:54px; letter-spacing:-1.5px;
               color:#1D1D1F; line-height:1.15;">
        Does popularity mean quality?
    </h1>
    <p style="font-size:19px; color:#6E6E73;">
        Exploring the relationship between book popularity
        and average ratings.
    </p>
</div>
""", unsafe_allow_html=True)


# Key statistics
col1, col2 = st.columns(2, gap="medium")

with col1:
    with st.container(border=True):
        st.metric("Pearson Correlation", f"{correlation:.3f}")
        st.caption("Negligible linear relationship")

with col2:
    with st.container(border=True):
        st.metric("Books Analyzed", f"{len(books):,}")
        st.caption("Goodreads titles")


st.write("")


# Main chart
with st.container(border=True):
    st.subheader("Popularity vs Average Rating")

    fig = plot_popularity(books)
    st.pyplot(fig, use_container_width=True)

    st.caption(
        "The horizontal axis uses a logarithmic scale "
        "to improve the visualization of book popularity."
    )


st.write("")


# Key insight
with st.container(border=True):
    st.markdown("**KEY INSIGHT**")

    st.subheader("More popular doesn't mean better rated.")

    st.write(
        "The Pearson correlation indicates a negligible positive "
        "linear relationship between book popularity and average rating. "
        "Books receiving more ratings do not necessarily have higher scores."
    )
