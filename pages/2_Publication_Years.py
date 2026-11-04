
import streamlit as st

from src.streamlit_data import load_cached_data
from src.analysis import publication_year_analysis
from src.plots import plot_publication_year


st.title("Publication Years & Average Rating")

st.write("Do average ratings differ across publication decades?")

# Load books dataset
books = load_cached_data("books.csv")

# Calculate average ratings by decade
decade_results = publication_year_analysis(books)


# Select decades with at least 30 books
available_decades = decade_results[decade_results["book_count"] >= 30]

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

# Filter selected decades
selected_decades = available_decades[
    (available_decades["decade"] >= year_range[0]) &
    (available_decades["decade"] <= year_range[1])
]

# Display line plot
fig = plot_publication_year(selected_decades)
st.pyplot(fig)

# Interpretation
st.write(
    "Average book ratings remain relatively stable across publication "
    "decades. No consistent increasing or decreasing trend is observed."
)

st.caption("The chart includes only decades with at least 30 books.")
