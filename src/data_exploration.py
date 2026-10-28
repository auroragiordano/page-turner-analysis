
from data_loader import load_data

##EXPLORATION OF BOOKS DATASET
books = load_data("books.csv")

print("\nDATASET INFORMATION")
books.info()

print("\nDESCRIPTIVE STATISTICS")
print(
    books[
        ["average_rating", "ratings_count", "original_publication_year"]
    ].describe()
)

print("\nMISSING VALUES")
print(books.isnull().sum())

print("\nDUPLICATED ROWS")
print(books.duplicated().sum())


##EXPLORATION OF RATINGS DATASET
ratings = load_data("ratings.csv")

print("\nRATINGS INFORMATION")
ratings.info()

print("\nMISSING VALUES")
print(ratings.isnull().sum())

print("\nDUPLICATED ROWS")
print(ratings.duplicated().sum())


##EXPLORATION OF TAGS DATASET
tags = load_data("tags.csv")

print("\nTAGS INFORMATION")
tags.info()

print("\nMISSING VALUES")
print(tags.isnull().sum())

print("\nDUPLICATED ROWS")
print(tags.duplicated().sum())


##EXPLORATION OF BOOK TAGS DATASET
book_tags = load_data("book_tags.csv")

print("\nBOOK_TAGS INFORMATION")
book_tags.info()

print("\nMISSING VALUES")
print(book_tags.isnull().sum())

print("\nDUPLICATED ROWS")
print(book_tags.duplicated().sum())


