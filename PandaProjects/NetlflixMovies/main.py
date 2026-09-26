import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

netflix_df = pd.read_csv(r'PandaProjects/NetlflixMovies/datasets/netflix_data.csv')

netflix_subset = netflix_df.loc[netflix_df.type != 'TV Show']
netflix_movies = netflix_subset.loc[:,['title','country','genre','release_year','duration']]
short_movies = netflix_movies.loc[netflix_movies['duration'] < 60]
colors = []
for index,value in netflix_movies.iterrows():
    genre = value.genre
    if genre == 'Children':
        colors.append('blue')
    elif genre == 'Documentaries':
        colors.append('green')
    elif genre == 'Stand-Up':
        colors.append('red')
    else:
        colors.append('yellow')


fig , ax = plt.subplots()
ax.scatter(netflix_movies['release_year'],netflix_movies['duration'],color=colors)
ax.set_xlabel('Release year')
ax.set_ylabel('Duration')
ax.set_title("Movie's Duration To the Movie's Release Date")

plt.show()