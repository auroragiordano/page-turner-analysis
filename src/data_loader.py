
import pandas as pd



def load_data(filename):
    """
    Load a Goodreads CSV file.

    Parameters:
        filename (str): Name of the CSV file.

    Returns:
        pd.DataFrame: Dataset loaded as a DataFrame.
    """
    try:
        return pd.read_csv("data/" + filename)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Dataset not found: {filename}"
        )



if __name__ == "__main__":
    books = load_data("books.csv")
    ratings = load_data("ratings.csv")
    tags = load_data("tags.csv")
    book_tags = load_data("book_tags.csv")

    print("Books:", books.shape)
    print("Ratings:", ratings.shape)
    print("Tags:", tags.shape)
    print("Book tags:", book_tags.shape)
