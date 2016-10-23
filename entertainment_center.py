# Author: John Nielsen
# Date: 10/12/16
# Description: This program is where all the magic happens. It imports all classes needed to render and play tralier site. It
#              calls the fresh_tomatoes.open_movies_page method which makes use of classes and writing html.

import movie
import tvShow
import fresh_tomatoes

movie_shelf = movie.load_movies()
tv_show_shelf = tvShow.load_tvshows()

video_library = movie_shelf + tv_show_shelf

fresh_tomatoes.open_movies_page(video_library)
