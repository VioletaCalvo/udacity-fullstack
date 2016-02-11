import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = open('templates/main.html').read()

# The main page layout and title bar
main_page_content = open('templates/main_content.html').read()

# A single movie entry html template
movie_tile_content = open('templates/movie_tile.html').read()

# A single tvshow entry html template
tvshow_tile_content = open('templates/tvshow_tile.html').read()

# Footer
footer = open('templates/footer.html').read()


# Extract the youtube id
def extract_youtube_id(youtube_url):
    """ Extract the youtube id from a youtube url

        Args:
            youtube_url (str) - the youtube url

        returns the youtube id
    """
    youtube_id_match = re.search(r'(?<=v=)[^&#]+', youtube_url)
    youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+',
                                                     youtube_url)
    youtube_id = (youtube_id_match.group(0) if youtube_id_match else None)
    return youtube_id


# Create video tiles content for movies or tvshows
def create_video_tiles_content(videos, type):
    """ Create the movie titles content

        Args:
            videos (array) - list of Movies or TvShow instances
            type (str) - type of video: 'movies' or 'tvshows'
    """
    # The HTML content for this section of the page
    content = ''
    # for each video in videos array:
    for video in videos:
        # Depending on type apend content
        if type is 'movies':
            # Append the tile for the movie with its content filled in
            content += movie_tile_content.format(
                movie_title=video.omdb_info['Title'],
                movie_year=video.omdb_info['Year'],
                movie_duration=video.omdb_info['Runtime'],
                movie_storyline=video.omdb_info['Plot'],
                movie_rating=video.omdb_info['imdbRating'],
                movie_genre=video.omdb_info['Genre'],
                poster_image_url=video.tmdb_poster,
                trailer_youtube_id=extract_youtube_id(video.trailer)
            )
        elif type is 'tvshows':
            # Append the tile for the tvshow with its content filled in
            content += tvshow_tile_content.format(
                tvshow_title=video.omdb_info['Title'],
                tvshow_duration=video.omdb_info['Runtime'],
                tvshow_storyline=video.omdb_info['Plot'],
                tvshow_rating=video.omdb_info['imdbRating'],
                tvshow_seasons=video.season_count,
                tvshow_genre=video.omdb_info['Genre'],
                poster_image_url=video.tmdb_poster,
                trailer_youtube_id=extract_youtube_id(video.trailer),
                opening_youtube_id=extract_youtube_id(video.opening)
            )
    return content


# Render content and open the videos page content
def open_media_page(movies, tvshows):
    """ Render content and open the videos page content

        Args:
            movies (array) - array of Movies instances
    """
    # Create or overwrite the output file
    output_file = open('website/fresh_tomatoes.html', 'w')

    # Replace the videos tiles placeholder generated content
    rendered_main_content = main_page_content.format(
        movie_tiles=create_video_tiles_content(movies, 'movies'),
        tvshow_tiles=create_video_tiles_content(tvshows, 'tvshows'),
        footer=footer)

    # Output the file
    rendered_main_head = main_page_head.format(
        main_content=rendered_main_content)

    output_file.write(rendered_main_head)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
