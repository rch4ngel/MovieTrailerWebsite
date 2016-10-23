# Author: John Nielsen
# Date: 10/14/16
# Description: This is the child class of video. Class contains specific attributes and methods for Movies.

# Import Parent class Video
import video
import urllib
import json
from collections import namedtuple

class Movie(video.Video):
    # TODO: Place __doc__ information here
    """Movie class is a subclass of Video. It inherites all of video's attributes and adds a instance variable of storyline."""

    # TODO: Define class variables

    # TODO: Write movie constructor __init__

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url, duration, rating):
        video.Video.__init__(self, title, poster_image_url, trailer_youtube_url, duration, rating)
        self.storyline = storyline

    # TODO: Define class instance variables

    # TODO: Define class instance Methods

def get_movies():
    api_url = 'http://localhost:3000/api/movies'

    # Fail gracefully if api_url isn't available.
    try:
        connection = urllib.urlopen(api_url)
        movies_json = connection.read()
    except IOError:
        print("Error: Cannot connect to node server")
        print("Using local json file")

        movies = [
                {
                    "title" : "The Recruit",
                    "storyline" : "A brilliant young CIA trainee is asked by his mentor to help find a mole in the Agency.",
                    "trailer_youtube_url" : "https://youtu.be/-aqecRSJo3o",
                    "poster_image_url" : "https://upload.wikimedia.org/wikipedia/en/6/62/Recruitmovie.jpg",
                    "duration" : "115",
                    "rating" : "PG13",
                    "isTvShow" : "false",
                    "season" : "",
                    "episode" : ""
                  },
                  {
                    "title" : "Street Fighter II",
                    "storyline" : "Two warriors fight to find their destiny.",
                    "trailer_youtube_url" : "https://youtu.be/_xlb65hp4lo",
                    "poster_image_url" : "http://www.gstatic.com/tv/thumb/dvdboxart/117849/p117849_d_v8_aa.jpg",
                    "duration" : "110",
                    "rating" : "R",
                    "isTvShow" : "false",
                    "season" : "",
                    "episode" : ""
                  },
                  {
                    "title" : "Ninja Scroll",
                    "storyline" : "A mysterious vagabond sets out on a journey to confront his past. Little does he know he is up against a demonic force of killers, with a ghost from his past as the leader.",
                    "trailer_youtube_url" : "https://youtu.be/9O6_N4mQBos",
                    "poster_image_url" : "http://www.gstatic.com/tv/thumb/dvdboxart/18789/p18789_d_v8_aa.jpg",
                    "duration" : "94",
                    "rating" : "R",
                    "isTvShow" : "false",
                    "season" : "",
                    "episode" : ""
                  },
                  {
                    "title" : "Gladiator",
                    "storyline" : "When a Roman general is betrayed and his family murdered by an emperor's corrupt son, he comes to Rome as a gladiator to seek revenge.",
                    "trailer_youtube_url" : "https://youtu.be/AxQajgTyLcM",
                    "poster_image_url" : "http://t3.gstatic.com/images?q=tbn:ANd9GcRuhegCaGHfcQc-Owpib9vGSO0hUlSUMTojO2s4ih8oXqHBw2ks",
                    "duration" : "155",
                    "rating" : "R",
                    "isTvShow" : "false",
                    "season" : "",
                    "episode" : ""
                  },
                  {
                    "title" : "Anchorman",
                    "storyline" : "Ron Burgundy is San Diego's top-rated newsman in the male-dominated broadcasting of the 1970s, but that's all about to change for Ron and his cronies when an ambitious woman is hired as a new anchor.",
                    "trailer_youtube_url" : "https://youtu.be/-T3wnP91OnI",
                    "poster_image_url" : "http://cdn.playbuzz.com/cdn/4dd5d1cf-9488-45f3-88d4-e1ca05d9a5e9/a78dfb31-1738-47fd-8134-171784a81719.jpg",
                    "duration" : "94",
                    "rating" : "PG13",
                    "isTvShow" : "false",
                    "season" : "",
                    "episode" : ""
                  },
                  {
                    "title" : "Trainwreck",
                    "storyline" : "Having thought that monogamy was never possible, a commitment-phobic career woman may have to face her fears when she meets a good guy.",
                    "trailer_youtube_url" : "https://youtu.be/2MxnhBPoIx4",
                    "poster_image_url" : "http://t2.gstatic.com/images?q=tbn:ANd9GcQUsANpZxgaSF9Wm3muDzN1f8QaZJGJ4VAT4NTsuKcgzBIUJLse",
                    "duration" : "125",
                    "rating" : "R",
                    "isTvShow" : "false",
                    "season" : "",
                    "episode" : ""
                  },
                  {
                    "title" : "A Night at the Roxbury",
                    "storyline" : "Two dim-witted brothers dream of owning their own dance club or at least getting into the coolest and most exclusive club in town, The Roxbury.",
                    "trailer_youtube_url" : "https://youtu.be/umnbOCVQphI",
                    "poster_image_url" : "https://upload.wikimedia.org/wikipedia/en/0/02/A_night_at_the_roxbury.jpg",
                    "duration" : "82",
                    "rating" : "PG13",
                    "isTvShow" : "false",
                    "season" : "",
                    "episode" : ""
                  },
                  {
                    "title" : "Aliens",
                    "storyline" : "he moon from Alien (1979) has been colonized, but contact is lost. This time, the rescue team has impressive firepower, but will it be enough?",
                    "trailer_youtube_url" : "https://youtu.be/XKSQmYUaIyE",
                    "poster_image_url" : "http://www.gstatic.com/tv/thumb/movieposters/9384/p9384_p_v8_av.jpg",
                    "duration" : "137",
                    "rating" : "R",
                    "isTvShow" : "false",
                    "season" : "",
                    "episode" : ""
                  },
                  {
                    "title" : "Never Back Down",
                    "storyline" : "A frustrated and conflicted teenager arrives at a new highschool to discover an underground fightclub and meet a classmate who begins to coerce him into fighting.",
                    "trailer_youtube_url" : "https://youtu.be/wtPB8z4MeCM",
                    "poster_image_url" : "https://upload.wikimedia.org/wikipedia/en/3/39/Never_back_down.jpg",
                    "duration" : "110",
                    "rating" : "PG13",
                    "isTvShow" : "false",
                    "season" : "",
                    "episode" : ""
                  },
                  {
                    "title" : "Interview with the vampire",
                    "storyline" : "Vampire tells the story of being immortal.",
                    "trailer_youtube_url" : "https://youtu.be/bDH7P0qvSMU",
                    "poster_image_url" : "http://t1.gstatic.com/images?q=tbn:ANd9GcQGafu-4fnvQNUYblHACTVjCkmWC8Ha1_qXqn-PKHf9Or6lsP6c",
                    "duration" : "110",
                    "rating" : "R",
                    "isTvShow" : "false",
                    "season" : "1",
                    "episode" : "1"
                  }
              ]
        movies_json = json.dumps(movies)

    else:
        connection.close()

    return movies_json

def object_decoder(obj):

    return Movie(obj['title'],
                 obj['storyline'],
                 obj['poster_image_url'],
                 obj['trailer_youtube_url'],
                 obj['duration'],
                 obj['rating'])
    return obj

def load_movies():
    movies_json = get_movies();

    movies = json.loads(movies_json, object_hook=object_decoder)

    return movies
