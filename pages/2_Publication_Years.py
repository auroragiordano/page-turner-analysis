
import streamlit as st

from src.streamlit_data import load_cached_data
from src.analysis import publication_year_analysis
from src.plots import plot_publication_year


# Load data
books = load_cached_data("books.csv")
decade_results = publication_year_analysis(books)

# Select decades with at least 30 books
available_decades = decade_results[
    decade_results["book_count"] >= 30
]


# Page introduction
st.markdown("""
<div style="text-align:center; padding:45px 10px 35px;">
    <p style="color:#6E6E73; font-size:13px; font-weight:600;">
        02 / PUBLICATION YEARS
    </p>
    <h1 style="font-size:54px; letter-spacing:-1.5px;
               color:#1D1D1F; line-height:1.15;">
        Does time change the story?
    </h1>
    <p style="font-size:19px; color:#6E6E73;">
        Exploring average book ratings across publication decades.
    </p>
</div>
""", unsafe_allow_html=True)


# Select publication period
year_range = st.slider(
    "Select publication decades",
    min_value=int(available_decades["decade"].min()),
    max_value=int(available_decades["decade"].max()),
    value=(
        int(available_decades["decade"].min()),
        int(available_decades["decade"].max())
    ),
    step=10
)

selected_decades = available_decades[
    (available_decades["decade"] >= year_range[0]) &
    (available_decades["decade"] <= year_range[1])
]


# Key statistics
col1, col2 = st.columns(2, gap="medium")

with col1:
    with st.container(border=True):
        st.metric("Decades Selected", len(selected_decades))
        st.caption("Decades with at least 30 books")

with col2:
    with st.container(border=True):
        st.metric(
            "Books Analyzed",
            f"{selected_decades['book_count'].sum():,}"
        )
        st.caption("Books in the selected decades")


st.write("")


# Main chart
with st.container(border=True):
    st.subheader("Average Rating by Publication Decade")

    fig = plot_publication_year(selected_decades)
    st.pyplot(fig, use_container_width=True)

    st.caption(
        "Only decades containing at least 30 books are displayed."
    )


st.write("")


# Key insight
with st.container(border=True):
    st.markdown("**KEY INSIGHT**")

    st.subheader("Great books are timeless.")

    st.write(
        "Average book ratings are generally similar across "
        "publication decades. The complete analysis does not "
        "show a consistent increasing or decreasing trend."
    )
