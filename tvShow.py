# Author: John Nielsen
# Date: 10/14/16
# Description: This is the child class of tv show. Class contains specific attributes and methods for TV Shows.

# import Parent class Video
import video
import urllib
import json
from collections import namedtuple

class TvShow(video.Video):
    # TODO: Place __doc__ information here
    """Tv show class is a subclass of Video and has inherited its variables and methods. TV show's special attributes are:
       season and episode"""

    # TODO: Define class variables

    # TODO: Write Tv Show constructor __init__
    def __init__(self, title, poster_image_url, trailer_youtube_url, duration, rating, season, episode):
        video.Video.__init__(self, title, poster_image_url, trailer_youtube_url, duration, rating)
        self.season = season
        self.episode = episode

    # TODO: Define class instance variables

    # TODO: Define class instance Methods

def get_tvshows():
    api_url = "http://localhost:3000/api/tvshows"

    try:
        connection = urllib.urlopen(api_url)
        tvshows_json = connection.read()
    except IOError:
        print("Error: Cannot connect to node server")
        print("Using local TV Shows")

        tvshows = [
                {
                    "title" : "Vampire Diaries",
                    "storyline" : "Teen girl is torn between two brothers.",
                    "trailer_youtube_url" : "https://youtu.be/72Tuuna9trM",
                    "poster_image_url" : "https://upload.wikimedia.org/wikipedia/en/5/52/The_Vampire_Diaries_Season_1.jpg",
                    "duration" : "110",
                    "rating" : "R",
                    "isTvShow" : "true",
                    "season" : "1",
                    "episode" : "1"
                }
            ]
        tvshows_json = json.dumps(tvshows)
    else:
        connection.close()

    return tvshows_json

def object_decoder(obj):
    return TvShow(obj['title'],
                  obj['poster_image_url'],
                  obj['trailer_youtube_url'],
                  obj['duration'],
                  obj['rating'],
                  obj['season'],
                  obj['episode'])

def load_tvshows():
    tvshows_json = get_tvshows()

    tvshows = json.loads(tvshows_json, object_hook=object_decoder)

    return tvshows
