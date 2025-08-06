# directly downloading fresh data from kaggle
# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows")
# print("Path to dataset files:", path)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# loading the data from csv 
movies_dp = pd.read_csv('imdb_top_1000.csv')
# print(movies_dp.info()) # for getting overview of the data 
# print('-'*50)


# All the methods :-

# Here we see that Gross, Released_Year and Runtime are of Object Dtype which should not be the scenario

# Runtime 
def clean_runtime():
    # print(movies_dp.head())
    # print(movies_dp['Runtime'])

    # Now for cleaning the Runtime column to convert it to Int64/int64 we can use following methods
    # 1. str.extract() with the regex as : r'(\d+)' , this covers all the scenarios/variations in which the data could be present
    # 2. str.replace(), this works for the current data set where we see the text to be removed always the same 

    # str.replace()
    # movies_dp['Runtime'] = movies_dp['Runtime'].str.replace(' min', '').astype('int64')
    # print(movies_dp['Runtime'])

    # str.extract()
    # print("Using str.extract() :")
    movies_dp['Runtime'] = movies_dp['Runtime'].str.extract(r'(\d+)').astype('int64')
    

print("\nRunning clean_runtime().....")
clean_runtime()

# Gross
def clean_gross() :
    # print(movies_dp['Gross'])
    # here as the data is present in 123,234,566 so regex scrapes only continous integers
    # hence using extract won't be a great choice using replace could better option 
    
    # movies_dp['Gross'] = movies_dp['Gross'].str.extract(r'(\d+)').astype('Int64')
    movies_dp['Gross'] = movies_dp['Gross'].str.replace(',', '').astype('Int64')
    # even more robust approch is present using regex
    # print(movies_dp['Gross'])

print("\nrunning clean_gross()......")
clean_gross()

# Released_Year
def clean_releasedYear():
    # there are 2 ways to converting Dtype of column to int64, one being using astype()
    # other one is using to_numeric()
    # print(movies_dp['Released_Year'])
    movies_dp['Released_Year'] = pd.to_numeric(movies_dp['Released_Year'], errors='coerce')
    # print(movies_dp['Released_Year'])

print('\nrunning clean_releasedYear()...')
clean_releasedYear()

# print(movies_dp.info())

# Next Step : Exploratory Analysis 

def data_distribution():
    # print(movies_dp['IMDB_Rating'])
    fig,ax = plt.subplots(1,3, figsize=(12,6))
    
    # IMDB rating distribution
    ax[0].hist(movies_dp['IMDB_Rating'], bins=10)
    ax[0].set_title('IMDB Ratings Distribution')
    ax[0].set_xlabel('IMDB Ratings')
    
    # Runtime distribution
    ax[1].hist(movies_dp['Runtime'], bins=10, color='orange')
    ax[1].set_title('Movies Runtime Distribution')
    ax[1].set_xlabel('Runtimes')

    # Release_Year distribution
    ax[2].hist(movies_dp['Released_Year'], bins=10, color='red')
    ax[2].set_title('Release Years Distribution')
    ax[2].set_xlabel('Released Years')

    plt.show()

# data_distribution()

def top_ten_directors():
    # print(movies_dp['Director'])
    # value_counts() method helps in counting the frequency of the entries, returns data in descending order
    # here head(10) - limits or makes the count to top 10 
    top_ten_director = movies_dp['Director'].value_counts().head(10)
    # print("\nTop 10 Directors to make to the List :")
    # print(top_ten_director)
    return top_ten_director

# top_ten_directors()

def genre_ratings():
    # print(movies_dp['Genre'])

    # as each movie have multiple genres it won't be possible analyse here
    # so we break each genre for each row that would create duplicate rows for movie entries with multiple genres
    # for that we do .spilt() then we explode(), which creates row for each genre

    movies_dp['Genre'] = movies_dp['Genre'].str.split(', ')
    movies_dp_exploded = movies_dp.explode('Genre') # need to create new dataframe for explode()
    # print(movies_dp_exploded)

    genre_Imdb_avg_ratings = movies_dp_exploded.groupby('Genre')['IMDB_Rating'].mean()
    # print('\nGenres avg ratings : ')
    # print(genre_Imdb_avg_ratings)
    return genre_Imdb_avg_ratings

# genre_ratings()

def plot_genreAndDirectorGraphs():
    directors = top_ten_directors()
    genres = genre_ratings()
    
    fig,ax = plt.subplots(1,2, figsize=(16,6))

    ax[0].barh(
        directors.index,
        directors.values
    )
    ax[0].set_title("Top 10 Directors in IMDb's Top 1000")
    ax[0].set_ylabel("Directors")

    ax[1].barh(
        genres.index,
        genres.values
    )
    ax[1].set_title("Average IMDb Rating by Genre")
    ax[1].set_ylabel("Genres")

    plt.show()

# plot_genreAndDirectorGraphs()

# Investigating correlations 

# using corr() method for getting correlations between different columns

def data_correlation():
    # before running correlation we need to remove or substitue / fill all the Nan values
    # I am dropping all the Nan values
    cleaned_movies_dp = movies_dp.dropna()
    print(cleaned_movies_dp.info())

    # before going for calling corr() its better to keep only numeric columns,
    # so that we don't see any failures while running corr() method

    only_numeric_dp = cleaned_movies_dp.select_dtypes(include=['number'])
    print("\nOnly numeric dataframe : ")
    print(only_numeric_dp.info())

    # .corr(), by default uses person method
    correlation_matrix = only_numeric_dp.corr()
    print("\nThe correlation matrix :")
    print(correlation_matrix)

# data_correlation()

# Analysing the relation between Runtime and IMDB_Rating 

def runtime_ImdbRating_realtion() :
    # print(movies_dp.info())
    plt.scatter(movies_dp['Runtime'], movies_dp['IMDB_Rating'])
    plt.xlabel("Movie Runtimes")
    plt.ylabel("IMDB Ratings")
    plt.title("Runtime v/s IMDB Ratings")
    plt.show()

# runtime_ImdbRating_realtion()