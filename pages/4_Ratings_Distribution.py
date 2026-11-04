
import streamlit as st

from src.streamlit_data import load_cached_data
from src.analysis import ratings_distribution_analysis
from src.plots import plot_ratings_distribution


st.title("Distribution of User Ratings")

st.write("How are user ratings distributed from 1 to 5 stars?")

# Load ratings dataset
ratings = load_cached_data("ratings.csv")

# Calculate rating frequencies
ratings_distribution = ratings_distribution_analysis(ratings)

# Display bar chart
fig = plot_ratings_distribution(ratings_distribution)
st.pyplot(fig)

# Interpretation
st.write(
    "User ratings are predominantly positive, with 4-star ratings "
    "being the most frequent. Approximately 69% of all ratings "
    "are either 4 or 5 stars."
)
