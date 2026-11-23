
import matplotlib.pyplot as plt


# Research Question 1: Are the most popular books also the highest-rated?
def plot_popularity(books):
    """Plot the relationship between popularity and average rating."""

    fig, ax = plt.subplots(figsize=(8, 5))

    # Create scatter plot
    ax.scatter(
        books["ratings_count"],
        books["average_rating"],
        alpha=0.2,
        s=10
    )

    ax.set_xscale("log")
    ax.set_xlabel("Number of ratings")
    ax.set_ylabel("Average rating")
    ax.set_title("Book Popularity vs Average Rating")

    fig.tight_layout()

    return fig


# Research Question 2: Do average ratings differ across publication decades?
def plot_publication_year(result):
    """Plot average book ratings by publication decade."""

    # Select decades with at least 30 books
    data = result[result["book_count"] >= 30]

    fig, ax = plt.subplots(figsize=(10, 5))

    # Create line plot
    ax.plot(
        data["decade"],
        data["average_rating"],
        marker="o"
    )

    ax.set_xlabel("Publication decade")
    ax.set_ylabel("Average rating (1–5)")
    ax.set_title("Average Book Rating by Publication Decade")
    ax.grid(alpha=0.3)

    fig.tight_layout()

    return fig


# Research Question 3: Which literary genres receive the highest average ratings?
def plot_genres(result):
    """Compare average book ratings across literary genres."""

    fig, ax = plt.subplots(figsize=(10, 5))

    # Create horizontal bar chart
    ax.barh(
        result["tag_name"],
        result["average_rating"]
    )

    ax.set_xlabel("Average rating (1–5)")
    ax.set_ylabel("Literary genre")
    ax.set_title("Average Book Rating by Genre")
    ax.invert_yaxis()

    fig.tight_layout()

    return fig


# Research Question 4: How are user ratings distributed from 1 to 5 stars?
def plot_ratings_distribution(result):
    """Plot the distribution of user ratings."""

    fig, ax = plt.subplots(figsize=(8, 5))

    # Create bar chart
    ax.bar(result.index, result.values)

    ax.set_xlabel("Rating (stars)")
    ax.set_ylabel("Number of ratings")
    ax.set_title("Distribution of User Ratings")
    ax.set_xticks([1, 2, 3, 4, 5])

    fig.tight_layout()

    return fig
