
import streamlit as st

from src.streamlit_data import load_cached_data
from src.analysis import popularity_analysis
from src.plots import plot_popularity


st.title("Popularity & Average Rating")

st.write("Are the most popular books also the highest-rated?")


# Load books dataset
books = load_cached_data("books.csv")

# Calculate Pearson correlation
correlation = popularity_analysis(books)

st.metric("Pearson correlation", f"{correlation:.3f}")

# Display scatter plot
fig = plot_popularity(books)
st.pyplot(fig)

# Interpretation
st.write(
    "The Pearson correlation indicates a very weak positive "
    "linear relationship between book popularity and average rating. "
    "More popular books are not necessarily better rated."
)
