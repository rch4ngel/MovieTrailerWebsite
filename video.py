# Author: John Nielsen
# Date: 10/14/16
# Description: This is the Parent class that will define global variables and methods for child classes movie and tv show.

# import fresh_tomatoes to open trailer
import fresh_tomatoes
import json

class Video:
    # TODO: Place __doc__ information here
    """Video class is the Parent class for media types such as Movies and TV Shows. Class variables duration and viewer_rating
        can be found herein."""

    # TODO: Define class variables
    VALID_RATINGS = ["G", "PG", "PG13", "R"]

    # TODO: Write video constructor __init__
    def __init__(self, title, poster_image_url, trailer_youtube_url,  duration, rating):
        # TODO: Define class instance variables
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.duration = duration
        self.rating = rating
