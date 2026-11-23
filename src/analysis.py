
import matplotlib.pyplot as plt

from src.data_loader import load_data
from src.data_cleaning import (
    clean_publication_year,
    remove_repeated_tags,
    remove_duplicates
)
from src.plots import (
    plot_popularity,
    plot_publication_year,
    plot_genres,
    plot_ratings_distribution
)


# Research Question 1: Are the most popular books also the highest-rated?
def popularity_analysis(books):
    """Analyze the relationship between popularity and average rating."""

    # Select the variables
    data = books[["ratings_count", "average_rating"]]

    # Descriptive statistics
    print("Descriptive statistics:")
    print(data.describe())

    # Pearson correlation
    correlation = data["ratings_count"].corr(data["average_rating"])
    print("\nPearson correlation:", round(correlation, 3))

    return correlation


# Research Question 2: Do average ratings differ across publication decades?
def publication_year_analysis(books):
    """Calculate average book ratings by publication decade."""

    # Remove missing publication years
    data = clean_publication_year(books).copy()

    # Create publication decades
    data["decade"] = (data["original_publication_year"] // 10 * 10).astype(int)

    # Calculate average ratings by decade
    result = (
        data.groupby("decade")
        .agg(
            average_rating=("average_rating", "mean"),
            book_count=("average_rating", "size")
        )
        .reset_index()
        .sort_values("decade")
    )

    print("\nAverage rating by publication decade:")
    print(result)

    return result


# Research Question 3: Which literary genres receive the highest average ratings?
def genre_analysis(books, book_tags, tags):
    """Calculate average book ratings by literary genre."""

    # Clean book-tag associations
    book_tags_clean = remove_repeated_tags(
        remove_duplicates(book_tags)
    )

    # Match tags with their names
    data = book_tags_clean.merge(
        tags,
        on="tag_id",
        how="left"
    )

    # Add book ratings
    data = data.merge(
        books[["goodreads_book_id", "average_rating"]],
        on="goodreads_book_id",
        how="inner"
    )

    # Select literary genres
    genres = [
        "fantasy", "romance", "mystery",
        "science-fiction", "historical-fiction",
        "horror", "thriller", "classics", "young-adult"
    ]

    data = data[data["tag_name"].isin(genres)]

    # Calculate average rating by genre
    result = (
        data.groupby("tag_name")
        .agg(
            average_rating=("average_rating", "mean"),
            book_count=("goodreads_book_id", "nunique")
        )
        .reset_index()
        .sort_values("average_rating", ascending=False)
    )

    print("\nAverage rating by literary genre:")
    print(result)

    return result


# Research Question 4: How are user ratings distributed from 1 to 5 stars?
def ratings_distribution_analysis(ratings):
    """Calculate the distribution of user ratings."""

    # Count ratings for each star value
    result = (
        ratings["rating"]
        .value_counts()
        .sort_index()
    )

    print("\nDistribution of user ratings:")
    print(result)

    return result


if __name__ == "__main__":
    books = load_data("books.csv")

    # Popularity analysis
    popularity_analysis(books)
    fig1 = plot_popularity(books)

    # Publication year analysis
    decade_results = publication_year_analysis(books)
    fig2 = plot_publication_year(decade_results)

    # Literary genres analysis
    book_tags = load_data("book_tags.csv")
    tags = load_data("tags.csv")
    genre_results = genre_analysis(books, book_tags, tags)
    fig3 = plot_genres(genre_results)

    # User ratings distribution
    ratings = load_data("ratings.csv")
    ratings_distribution = ratings_distribution_analysis(ratings)
    fig4 = plot_ratings_distribution(ratings_distribution)

    # Display all plots
    plt.show()
