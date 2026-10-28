
from data_loader import load_data


def remove_duplicates(df):
    """Remove fully duplicated rows."""
    return df.drop_duplicates()


def remove_repeated_tags(df):
    """Keep the highest count for each book-tag pair."""
    return (
        df.sort_values("count", ascending=False)
        .drop_duplicates(subset=["goodreads_book_id", "tag_id"])
    )


def clean_publication_year(df):
    """Remove books with missing publication years."""
    return df.dropna(subset=["original_publication_year"])


if __name__ == "__main__":
    # Clean book-tag associations
    book_tags = load_data("book_tags.csv")
    book_tags_clean = remove_duplicates(book_tags)
    book_tags_clean = remove_repeated_tags(book_tags_clean)

    print("Original book-tag rows:", len(book_tags))
    print("Cleaned book-tag rows:", len(book_tags_clean))

    # Clean missing publication years
    books = load_data("books.csv")
    books_year_clean = clean_publication_year(books)

    print("Books with publication year:", len(books_year_clean))

    # Check rating values
    ratings = load_data("ratings.csv")
    invalid_ratings = (ratings["rating"] < 1) | (ratings["rating"] > 5)

    print("Invalid ratings:", invalid_ratings.sum())
