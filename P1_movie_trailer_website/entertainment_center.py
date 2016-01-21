# import required libraries
import fresh_tomatoes
import media
import csv

# Create the movies array of Movies calss instances
# Movie class constructor takes only two arguments (see media.py)
# movies list is read from data/movies.csv file (only title_query and trailer
#  is needed)
movies = []
with open('data/movies.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movies.append(media.Movie(row['title_query'], row['trailer']))

# Create the tvshows array of TvShow calss instances
# TvShow class constructor takes only three arguments (see media.py)
# tvshows list is read from data/movies.csv file (only title_query and trailer
#  is needed)
tvshows = []
with open('data/tvshows.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        tvshows.append(media.TvShow(row['title_query'], row['seasons_count'],
                                    row['trailer'], row['opening_video']))

# Use fresh tomatoes to generate HTML dinamicaly
# fresh_tomatoes.render_tvshows_page(tvshows)
fresh_tomatoes.open_media_page(movies, tvshows)
