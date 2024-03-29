import numpy as np
import pandas as pd

column_names = ['color', 'director_name', 'num_critic_for_reviews', 'duration', 'gross', 'movie_title',
                'num_user_for_reviews',	'country', 'cotent_rating',	'budget', 'title_year',	'imdb_score', 'genre']

# Import CSV into df
df = pd.read_csv('moives.csv', sep='|', header=None, names=column_names, na_values='?', thousands=',', skiprows=3)
