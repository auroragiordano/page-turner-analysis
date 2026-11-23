
import streamlit as st


# Hero section with minimalist book illustration
st.markdown("""
<style>
.hero-wrapper {
    background: linear-gradient(180deg, #F5FAFF 0%, #EAF4FF 100%);
    border: 1px solid #D6E6F5;
    border-radius: 32px;
    padding: 30px 20px 20px;
    margin-bottom: 28px;
}

.hero {
    text-align: center;
    padding: 35px 20px 55px;
}

.book-motif {
    display: flex;
    justify-content: center;
    align-items: flex-end;
    gap: 10px;
    margin-bottom: 26px;
}

.book-motif span {
    display: inline-block;
    width: 16px;
    border-radius: 5px;
    background: linear-gradient(180deg, #CFE6FA 0%, #8EC5F6 100%);
    box-shadow: 0 4px 10px rgba(0, 113, 227, 0.08);
}

.book-motif span:nth-child(1) {
    height: 46px;
    transform: rotate(-6deg);
}

.book-motif span:nth-child(2) {
    height: 58px;
    background: linear-gradient(180deg, #B9DBF8 0%, #6FB2EE 100%);
}

.book-motif span:nth-child(3) {
    height: 52px;
    transform: rotate(4deg);
}

.book-motif span:nth-child(4) {
    height: 62px;
    background: linear-gradient(180deg, #D9ECFD 0%, #A8D1F5 100%);
}

.book-motif span:nth-child(5) {
    height: 48px;
    transform: rotate(-3deg);
}

.hero h1 {
    font-size: clamp(42px, 6vw, 76px);
    font-weight: 700;
    letter-spacing: -2px;
    line-height: 1.1;
    color: #1D1D1F;
    margin-bottom: 0;
}

.hero p {
    font-size: 21px;
    color: #6E6E73;
    margin-top: 24px;
}
</style>

<div class="hero-wrapper">
    <div class="hero">
        <div class="book-motif" aria-hidden="true">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
        </div>
        <h1>Discover what makes<br>a book great.</h1>
        <p>Explore 10,000 books and millions of Goodreads ratings.</p>
    </div>
</div>
""", unsafe_allow_html=True)


# Dataset overview
st.header("The dataset at a glance.")

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    with st.container(border=True):
        st.metric("Books", "10,000")

with col2:
    with st.container(border=True):
        st.metric("User Ratings", "5,976,479")

with col3:
    with st.container(border=True):
        st.metric("Unique Tags", "34,252")


st.write("")
st.write("")


# Interactive discoveries
st.header("The story behind the numbers.")
st.write("Every book has a story. So does the data.")

insights = {
    "Popularity": {
        "value": "0.045",
        "label": "Pearson correlation",
        "title": "Famous doesn't always mean better.",
        "description": (
            "Book popularity has almost no linear relationship "
            "with average rating."
        ),
        "color": "#0071E3"
    },
    "Genres": {
        "value": "4.058",
        "label": "Fantasy average rating",
        "title": "A little magic goes a long way.",
        "description": (
            "Fantasy receives the highest average rating among "
            "the selected literary categories."
        ),
        "color": "#9D77C2"
    },
    "Ratings": {
        "value": "69%",
        "label": "4 and 5-star ratings",
        "title": "Readers tend to see the bright side.",
        "description": (
            "Around 69% of user ratings are either "
            "four or five stars."
        ),
        "color": "#D58F42"
    }
}

# Choose a discovery
selection = st.segmented_control(
    "Explore a discovery",
    options=list(insights),
    default="Popularity"
)

insight = insights[selection]

# Display selected discovery
with st.container(border=True):
    st.markdown(
        f"<h1 style='color:{insight['color']}; "
        f"font-size:64px; margin-bottom:0'>"
        f"{insight['value']}</h1>",
        unsafe_allow_html=True
    )

    st.caption(insight["label"])
    st.subheader(insight["title"])
    st.write(insight["description"])


st.write("")
st.write("")


# Research questions
st.header("Four questions. New perspectives.")

col1, col2 = st.columns(2, gap="medium")

with col1:
    with st.container(border=True):
        st.subheader("01. Popularity")
        st.write(
            "Are the most popular books also the highest-rated?"
        )

    with st.container(border=True):
        st.subheader("03. Literary Genres")
        st.write(
            "Which genres tend to receive the highest ratings?"
        )

with col2:
    with st.container(border=True):
        st.subheader("02. Publication Years")
        st.write(
            "Are older books rated differently from newer books?"
        )

    with st.container(border=True):
        st.subheader("04. User Ratings")
        st.write(
            "How are Goodreads user ratings distributed?"
        )


st.write("")

# Navigation message
st.info("Select a page from the sidebar to explore the analyses.")
