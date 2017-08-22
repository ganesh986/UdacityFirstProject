#!/usr/bin/env python
import webbrowser


class Movie():

    """This class provides a way to store movie related informations"""

    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        """
        Inizialize Instance of Movie Class
        :param movie_title: string
        :param movie_storyline: string
        :param poster_image: string
        :param trailer_youtube: string
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Inizialize Instance for opening youtube trailer
        :return: webbrowser to play video
        """
        webbrowser.open(self.trailer_youtube_url)
