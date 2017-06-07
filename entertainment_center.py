import media
from lib import fresh_tomatoes

casino_royale = media.Movie("Casino Royale",
                            "James Bond takes on a new enemy Le Chiffre, in a game of poker more important that ever",
                            "http://static.rogerebert.com/uploads/movie/movie_poster/casino-royale-2007/large_toEaueEfDxX57y4J5MRRA7qsy5K.jpg",
                            "https://www.youtube.com/watch?v=xK7PbujRUOk")

dark_knight = media.Movie("The Dark Knight",
                          "Batman takes on the greatest villain of all time: The Joker",
                          "http://static.rogerebert.com/uploads/movie/movie_poster/the-dark-knight-2008/large_1hRoyzDtpgMU7Dz4JF22RANzQO7.jpg",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY")

skyfall = media.Movie("Skyfall",
                      "James Bond proves that age is just a number",
                      "http://img.goldposter.com/2015/11/Skyfall_poster_goldposter_com_101.jpg@0o_0l_400w_70q.jpg",
                      "https://www.youtube.com/watch?v=6kw1UVovByw")

django = media.Movie("Django Unchained",
                     "One slave with eyes on one prize",
                     "https://s-media-cache-ak0.pinimg.com/736x/99/a1/98/99a198f4af6aafea574cdd4b89ef5daa.jpg",
                     "https://www.youtube.com/watch?v=eUdM9vrCbow")

wolf_of_wall_street = media.Movie("Wolf of Wall Street",
                                  "It's amazing what money can create. And destroy",
                                  "https://s-media-cache-ak0.pinimg.com/originals/dd/69/7f/dd697f3667c5d22e24f4b4431099ab32.jpg",
                                  "https://www.youtube.com/watch?v=iszwuX1AK6A")

focus = media.Movie("Focus",
                    "Always be two steps ahead of the competition",
                    "http://i.axs.com/2016/07/promoted-media-optimized_5788e78687c84.jpg",
                    "https://www.youtube.com/watch?v=MxCRgtdAuBo")


movies = [casino_royale, dark_knight, skyfall, django, wolf_of_wall_street, focus]

fresh_tomatoes.open_movies_page(movies)
