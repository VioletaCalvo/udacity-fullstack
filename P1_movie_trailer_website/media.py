# media.py
# Violeta Calvo Ilundain - 2015
#
# class Video
# class Movie(Video)
# class TvShow(Video)

# import
import webbrowser
import json  # this library is used to read response from OMDb API
import urllib
import tmdb3 # 'pip install tmdb3' in the console
import config

tmdb3.set_key(config.tmdb_key)

class Video():
    """ A general video calss to store video information
        This class retrieves video information from the OMDb API

        Args:
            video_query (str): the video title query
            video_type (str): in ['MOVIE', 'SERIES']

        Atributes:
            omdb_info (dict): the movie info by OMDb in python dict format
            tmdb_poster (str): the movie poster image url
    """
    def __init__(self, video_query, video_type):
        self.set_omdb_info(video_query.replace(' ', '+'))
        self.set_poster(video_query, video_type)

    # Retrieve video info from OMDb API
    def set_omdb_info(self, title_query):
        omdb_url = "http://www.omdbapi.com/?t="
        query = "&y=&plot=short&r=json"
        url = omdb_url+title_query+query
        connection = urllib.urlopen(url)
        output = connection.read()
        connection.close()
        self.omdb_info = json.loads(output)

    # OMDB doesn't allows image links unless you donated
    # for the poster I use the movie database
    def set_poster(self, title_query, video_type):
        if video_type is 'MOVIE':
            tmdb_id = tmdb3.searchMovie(title_query)[0].id
            video = tmdb3.Movie(tmdb_id)
        else:
            tmdb_id = tmdb3.searchSeries(title_query)[0].id
            video = tmdb3.Series(tmdb_id)
        self.tmdb_poster = video.poster.geturl('w342')


class Movie(Video):
    """ This class provides a way to store movie related information
        This class is Video class child

        Args:
            movie_query (str): the movie title query
            trailer_url (str): the youtube trailer url

        Atributes:
            omdb_info (dict): the movie info by OMDb in python dict format
            trailer (str): the youtube movie trailer url
    """

    # Constructor
    def __init__(self, movie_query, trailer_url):
        Video.__init__(self, movie_query, 'MOVIE')
        self.trailer = trailer_url

    # Methods
    def show_trailer(self):
        webbrowser.open(self.trailer)


class TvShow(Video):
    """ This class provides a way to store tv show related information
        This class is Video class child.

        Args:
            tv_query (str): the movie title query
            trailer_url (str): the youtube pilote episode url
            opening_url (str): the youtube opening url
            season_count (str): the number of seasons

        Atributes:
            omdb_info (dict): the tvshow info by OMDb in python dict format
            trailer (str): the youtube tvshow trailer url
            opening (str): the youtube opening url
            season_count (str): the number of seasons
    """

    # Constructor
    def __init__(self, tv_query, season_count, trailer_url, opening_url):
        Video.__init__(self, tv_query, 'SERIES')
        self.trailer = trailer_url
        self.opening = opening_url
        self.season_count = season_count

    # Methods
    def show_opening(self):
        webbrowser.open(self.opening_video)

    def show_trailer(self):
        webbrowser.open(self.trailer)
