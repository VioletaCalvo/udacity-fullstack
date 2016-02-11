# P1: Movie Trailer Website

A website created for the first Project of Udacity's [Full Stack Web Developper Nanodegree] (https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Features

This project creates a website with a list of favourites movies and tv series. The lists of movies and series are taken from two csv files. The website is generated dinamicaly by a pathon data structure.
This project uses OMDb API to retrieve movie and tv series info.

This project uses TMDb API to retrieve movie and tv series posters. OMDb link images are forbidden.

## How to run

### Requieriments

To run the `entertainment_center.py` you need the tmdb3 python module and a TMDb api key.

#### TMDb python module
You need to install `tmdb3` python module. You can do it via the bash shell with this command:

```sh
pip install tmdb3
```

#### The Movie Database API key

Also you need to configure your _The Movie Database_ api key in config.py file. If you don't have one go to https://www.themoviedb.org and request for an api key.

### Run

Clone this repository and run `entertainment_center.py` in your python console.

Alternatively you can launch `website/fresh_tomatoes.html`.

See the [live website here](http://violetacalvo.github.io/udacity-fullstack/P1_movie_trailer_website/website/fresh_tomatoes.html).
