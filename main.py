# directly downloading fresh data from kaggle
# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows")
# print("Path to dataset files:", path)

import pandas as pd

# loading the data from csv 
movies_dp = pd.read_csv('imdb_top_1000.csv')
print(movies_dp)