
import streamlit as st

from src.streamlit_data import load_cached_data
from src.analysis import ratings_distribution_analysis
from src.plots import plot_ratings_distribution


# Load data
ratings = load_cached_data("ratings.csv")
ratings_distribution = ratings_distribution_analysis(ratings)

# Calculate summary statistics
most_common_rating = ratings_distribution.idxmax()

positive_percentage = (
    ratings_distribution.loc[[4, 5]].sum()
    / ratings_distribution.sum()
    * 100
)


# Page introduction
st.markdown("""
<div style="text-align:center; padding:45px 10px 35px;">
    <p style="color:#6E6E73; font-size:13px; font-weight:600;">
        04 / RATINGS DISTRIBUTION
    </p>
    <h1 style="font-size:54px; letter-spacing:-1.5px;
               color:#1D1D1F; line-height:1.15;">
        What do readers really think?
    </h1>
    <p style="font-size:19px; color:#6E6E73;">
        Exploring millions of user ratings,
        one star at a time.
    </p>
</div>
""", unsafe_allow_html=True)


# Key statistics
col1, col2 = st.columns(2, gap="medium")

with col1:
    with st.container(border=True):
        st.metric(
            "Most Common Rating",
            f"{most_common_rating} ★"
        )
        st.caption("Most frequently assigned score")

with col2:
    with st.container(border=True):
        st.metric(
            "Positive Ratings",
            f"{positive_percentage:.1f}%"
        )
        st.caption("Ratings of 4 or 5 stars")


st.write("")


# Main chart
with st.container(border=True):
    st.subheader("Distribution of User Ratings")

    fig = plot_ratings_distribution(ratings_distribution)
    st.pyplot(fig, use_container_width=True)

    st.caption(
        "Frequency of individual user ratings from 1 to 5 stars."
    )


st.write("")


# Key insight
with st.container(border=True):
    st.markdown("**KEY INSIGHT**")

    st.subheader("Readers tend to see the bright side.")

    st.write(
    f"User ratings are predominantly positive. "
    f"Approximately {positive_percentage:.1f}% of all ratings "
    f"are either four or five stars, with {most_common_rating} "
    f"being the most frequently assigned score."
)
