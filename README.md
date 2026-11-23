# Page Turners Analysis

Page Turners is a Python data analysis project that explores book popularity and user ratings using the Goodreads-10k dataset. The project includes data cleaning, descriptive statistical analysis, visualizations, and an interactive Streamlit dashboard.

## Project Objectives

The analysis focuses on four research questions:

1. Is there a relationship between a book's popularity and its average rating?
2. Are older books rated differently from recently published books?
3. Which literary genres tend to receive the highest average ratings?
4. How are Goodreads user ratings distributed?

## Dataset

The project uses the [goodbooks-10k dataset](https://github.com/zygmuntz/goodbooks-10k), containing information about 10,000 books and approximately 6 million user ratings.

Four CSV files are used:

- `books.csv`: book information, average ratings, popularity, and publication years.
- `ratings.csv`: individual user ratings from 1 to 5 stars.
- `tags.csv`: names and identifiers of user-generated tags.
- `book_tags.csv`: associations between books and tags.

The datasets are not included in this repository. They must be downloaded separately from the original dataset source and placed inside the `data/` folder.

## Technologies

The project uses Python and the following tools:

- **pandas:** data loading, cleaning, and analysis.
- **Matplotlib:** statistical visualizations.
- **Streamlit:** interactive multipage dashboard.
- **Git and GitHub:** version control.

Additional Python dependencies are listed in `requirements.txt`.

## Project Structure

```text
page-turner-analysis/
├── .streamlit/
│   └── config.toml
├── data/
│   ├── books.csv
│   ├── ratings.csv
│   ├── tags.csv
│   └── book_tags.csv
├── pages/
│   ├── 1_Popularity.py
│   ├── 2_Publication_Years.py
│   ├── 3_Literary_Genres.py
│   └── 4_Ratings_Distribution.py
├── src/
│   ├── data_loader.py
│   ├── data_exploration.py
│   ├── data_cleaning.py
│   ├── analysis.py
│   ├── plots.py
│   └── streamlit_data.py
├── app.py
├── home.py
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: The CSV files shown under `data/` must be downloaded separately. The `.venv/` virtual environment is also excluded from version control.*

## Installation and Usage

1. Clone the repository and open the project folder.

2. Create and activate a Python virtual environment (macOS/Linux):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required libraries:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Create the data folder if it does not already exist:

   ```bash
   mkdir -p data
   ```

5. Download `books.csv`, `ratings.csv`, `tags.csv`, and `book_tags.csv` from the [goodbooks-10k repository](https://github.com/zygmuntz/goodbooks-10k) and place them inside `data/`.

6. Start the Streamlit dashboard from the project root:

   ```bash
   python -m streamlit run app.py
   ```

The application will usually be accessible locally at [http://localhost:8501](http://localhost:8501).

## Streamlit Dashboard

The dashboard contains five pages:

- **Home:** project overview, dataset information, and research objectives.
- **Popularity & Ratings:** scatter plot and Pearson correlation coefficient.
- **Publication Years:** average ratings by publication decade with an interactive time-range filter.
- **Literary Genres:** comparison of selected literary categories with a Top 3/5/9 filter.
- **Ratings Distribution:** distribution of individual user ratings from 1 to 5 stars.

The application uses cached data loading to avoid repeatedly reading the CSV files.

## Notes

The analysis is descriptive and based on the available Goodreads data.

- Literary categories are identified using user-generated tags, and books may belong to multiple categories.
- The average rating for each genre is calculated as an **unweighted arithmetic mean of the books' average ratings**. Each book contributes equally, regardless of its number of individual user ratings.
- The publication-year chart includes only decades containing at least 30 books.
- The Pearson correlation measures linear association and does not imply causation.
