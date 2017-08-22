#!/usr/bin/env python

# import of the modules
import media
import fresh_tomatoes
import os

# define of the movies
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://images-na.ssl-images-amazon.com/images/I/51NpxQ0ma8L.jpg",  # noqa
                        "https://www.youtube.com/watch?v=gCrTZMA_Mm4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://images.movieplayer.it/images/2010/03/25/la-copertina-di-avatar-dvd-150956.jpg",  # noqa
                     "https://www.youtube.com/watch?v=moSRMC5JNww")

kill_bill = media.Movie("Kill Bill",
                        "A story of revenge",
                        "https://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg",  # noqa
                        "https://www.youtube.com/watch?v=7kSuas6mRpk")

reservoir_dogs = media.Movie("Reservoir Dogs",
                        """After a simple jewelry heist goes terribly wrong,
                        the surviving criminals begin to suspect that one of
                        them is a police informant.""",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BZmExNmEwYWItYmQzOS00YjA5LTk2MjktZjEyZDE1Y2QxNjA1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",  # noqa
                        "https://www.youtube.com/watch?v=vayksn4Y93A")

fight_club = media.Movie("Fight Club",
                        """An insomniac office worker, looking for a way to
                        change his life, crosses paths with a devil-may-care
                        soap maker, forming an underground fight club that
                        evolves into something much, much more.""",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BZGY5Y2RjMmItNDg5Yy00NjUwLThjMTEtNDc2OGUzNTBiYmM1XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg",  # noqa
                        "https://www.youtube.com/watch?v=FEqp8tSh1F4")

pulp_fiction = media.Movie("Pulp Fiction",
                        """After a simple jewelry heist goes terribly wrong,
                        the surviving criminals begin to suspect that one of
                        them is a police informant.""",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_SY1000_CR0,0,673,1000_AL_.jpg",  # noqa
                        "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

# Array with movies list to pass to open_movies_page method
movies = [toy_story,
          avatar,
          kill_bill,
          reservoir_dogs,
          fight_club,
          pulp_fiction]

fresh_tomatoes.open_movies_page(movies)
