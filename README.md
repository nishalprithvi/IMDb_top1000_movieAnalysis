# 🎬 IMDb Top 1000 Movies: An Exploratory Data Analysis

A deep dive into the IMDb Top 1000 movie dataset to uncover the patterns and characteristics of critically acclaimed films. This project cleans, analyzes, and visualizes data to answer key questions about what makes a movie "great."

---

## 🎯 Project Goals

This analysis sought to answer the following questions:
* What are the typical distributions of movie ratings, runtimes, and release years?
* Who are the most prolific directors and what are the most common genres in the top 1000 list?
* Which genres, on average, receive the highest ratings?
* Is there a correlation between a movie's runtime, its financial success (Gross), and its IMDb rating?

---

## 💾 Dataset

The dataset used is the **IMDb Top 1000 Movies & TV Shows**, sourced from Kaggle.

* **Source:** [IMDb Movies Dataset on Kaggle](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows)
* **Content:** Contains 1000 rows of movie data, with columns including `Series_Title`, `Released_Year`, `IMDB_Rating`, `Director`, `Genre`, `Runtime`, and `Gross` earnings.

---

## 🛠️ Tech Stack

* **Python 3**
* **Pandas:** For data manipulation, cleaning, and aggregation.
* **NumPy:** For numerical operations.
* **Matplotlib:** For data visualization and plotting.

---

## ⚙️ Project Workflow

The analysis was conducted in a structured, step-by-step manner:

### 1. Data Loading and Inspection
* The `imdb_top_1000.csv` file was loaded into a Pandas DataFrame.
* Initial inspection using `.info()` and `.head()` revealed data quality issues in several key columns.

### 2. Data Cleaning and Preparation
* **`Runtime`:** Cleaned the column by removing the " min" suffix and converting the data type from `object` to `int64`.
* **`Gross`:** Removed comma separators from the string values and converted the column to a nullable `Int64` type to handle missing values.
* **`Released_Year`:** Handled non-numeric entries by using `pd.to_numeric` with `errors='coerce'`, which gracefully converted problematic values to `NaN`.
* **`Genre`:** Processed the multi-value genre strings by splitting them and using `.explode()` to create a tidy dataset where each row represents a single movie-genre combination.

### 3. Exploratory Analysis & Visualization

Several visualizations were created to uncover insights:

* **Histograms:** To understand the distribution of `IMDB_Rating`, `Runtime`, and `Released_Year`.
* **Horizontal Bar Charts:**
    * To visualize the **Top 10 Most Frequent Directors**.
    * To display the **Average IMDb Rating by Genre**.

### 4. Correlation Analysis
* A correlation matrix was calculated for all numeric columns to quantify the relationships between variables like `IMDB_Rating`, `Runtime`, and `Gross`.
* A **scatter plot** was created to specifically visualize the relationship between movie `Runtime` and `IMDB_Rating`.

---

## ✨ Key Findings

* **Top Directors:** Directors like **Alfred Hitchcock**, **Steven Spielberg**, and **Martin Scorsese** are among the most frequent, indicating their consistent ability to produce critically acclaimed films.
* **Highest-Rated Genres:** While common, genres like 'Action' do not have the highest average ratings. Niche genres like **'Film-Noir'**, **'Western'**, and **'War'** tend to have higher average IMDb ratings.
* **Distributions:** Most top-rated movies have a runtime between **100 and 150 minutes**, and the majority have an IMDb rating between **7.7 and 8.1**.
* **Correlations:** A weak positive correlation was found between `Runtime` and `IMDB_Rating`, suggesting that slightly longer movies tend to have slightly higher ratings, but it is not a strong relationship.

---

## 🚀 How to Run the Code

1.  **Clone the repository or download the source code.**
2.  **Ensure you have the required libraries installed:**
    ```bash
    pip install pandas numpy matplotlib
    ```
3.  **Place the `imdb_top_1000.csv` file in the same directory as the script.**
4.  **Run the Python script:**
    ```bash
    python main.py
    ```
    *(Uncomment the function calls at the end of the script to see the outputs and plots.)*

---

## 🔮 Future Work

* **Analyze Trends Over Time:** Investigate how average runtimes, popular genres, and ratings have evolved across different decades.
* **Actor Analysis:** Perform a similar analysis on the `Star1`, `Star2`, etc., columns to find the most prolific and highest-rated actors.
* **Natural Language Processing (NLP):** Analyze the movie `Overview` text to find common themes or keywords in highly-rated films.