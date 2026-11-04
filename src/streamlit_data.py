
import streamlit as st
from src.data_loader import load_data


@st.cache_data
def load_cached_data(filename):
    """Load and cache a Goodreads dataset."""
    return load_data(filename)
