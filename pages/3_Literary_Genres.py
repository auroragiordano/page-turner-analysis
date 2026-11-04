
import streamlit as st

from src.streamlit_data import load_cached_data
from src.analysis import genre_analysis
from src.plots import plot_genres


st.title("Literary Genres & Average Rating")

st.write("Which literary genres receive the highest average ratings?")

# Load datasets
books = load_cached_data("books.csv")
book_tags = load_cached_data("book_tags.csv")
tags = load_cached_data("tags.csv")

# Calculate average ratings by genre
genre_results = genre_analysis(books, book_tags, tags)


# Select number of genres
top_n = st.selectbox(
    "Number of genres to display",
    options=[3, 5, 9],
    index=2
)

# Display selected genres
selected_genres = genre_results.head(top_n)

fig = plot_genres(selected_genres)
st.pyplot(fig)

# Interpretation
st.write(
    f"Displaying the top {top_n} literary categories by average rating. "
    "Fantasy has the highest average rating among the selected categories, "
    "although differences across genres are relatively small."
)

st.caption(
    "Books can belong to multiple categories. "
    "Each book contributes equally to the average rating of its categories."
)
