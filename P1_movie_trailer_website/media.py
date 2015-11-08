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


class Video():
    """ A general video calss to store video information
        This class retrieves video information from the OMDb API

        Args:
            video_query (str): the video title query

        Atributes:
            omdb_info (dict): the movie info by OMDb in python dict format
    """
    def __init__(self, video_query):
        self.set_omdb_info(video_query.replace(' ', '+'))

    # Retrieve video info from OMDb API
    def set_omdb_info(self, title_query):
        omdb_url = "http://www.omdbapi.com/?t="
        query = "&y=&plot=short&r=json"
        url = omdb_url+title_query+query
        connection = urllib.urlopen(url)
        output = connection.read()
        connection.close()
        self.omdb_info = json.loads(output)


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
        Video.__init__(self, movie_query)
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
        Video.__init__(self, tv_query)
        self.trailer = trailer_url
        self.opening = opening_url
        self.season_count = season_count

    # Methods
    def show_opening(self):
        webbrowser.open(self.opening_video)

    def show_trailer(self):
        webbrowser.open(self.trailer)
