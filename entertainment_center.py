import media
from lib import fresh_tomatoes

# Creating 6 instances of Movie and assigning them to variables
casino_royale = media.Movie(
    "Casino Royale",
    "James Bond takes on a new enemy Le Chiffre, in a game of poker "
    "more important that ever",
    "http://static.rogerebert.com/uploads/movie/movie_poster/casino-royale-2007/large_toEaueEfDxX57y4J5MRRA7qsy5K.jpg",  # NOQA
    "https://www.youtube.com/watch?v=xK7PbujRUOk")

dark_knight = media.Movie(
    "The Dark Knight",
    "Batman takes on the greatest villain of all time: The Joker",
    "http://static.rogerebert.com/uploads/movie/movie_poster/the-dark-knight-2008/large_1hRoyzDtpgMU7Dz4JF22RANzQO7.jpg",  # NOQA
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

skyfall = media.Movie(
    "Skyfall",
    "James Bond proves that age is just a number",
    "https://s-media-cache-ak0.pinimg.com/originals/af/cc/dd/afccdd56da1292f3c0be28804e557723.jpg",  # NOQA
    "https://www.youtube.com/watch?v=6kw1UVovByw")

django = media.Movie(
    "Django Unchained",
    "One slave with eyes on one prize",
    "https://s-media-cache-ak0.pinimg.com/736x/99/a1/98/99a198f4af6aafea574cdd4b89ef5daa.jpg",  # NOQA
    "https://www.youtube.com/watch?v=eUdM9vrCbow")

wolf_of_wall_street = media.Movie(
    "Wolf of Wall Street",
    "It's amazing what money can create. And destroy",
    "https://s-media-cache-ak0.pinimg.com/originals/dd/69/7f/dd697f3667c5d22e24f4b4431099ab32.jpg",  # NOQA
    "https://www.youtube.com/watch?v=iszwuX1AK6A")

focus = media.Movie(
    "Focus",
    "Always be two steps ahead of the competition",
    "http://i.axs.com/2016/07/promoted-media-optimized_5788e78687c84.jpg",
    "https://www.youtube.com/watch?v=MxCRgtdAuBo")

# Placing the variables of Movie instances inside an array
movies = [casino_royale, dark_knight,
          skyfall, django, wolf_of_wall_street, focus]

# Passing the movies array to fresh_tomatoes to generate
# the webpage and open it
fresh_tomatoes.open_movies_page(movies)
