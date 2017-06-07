import webbrowser

class Movie():
    """This function provides a way to create movie instances of only the
    coolest and best movies and put them on a totally rad HTML site"""

    def __init__(self, title, storyline, poster_image, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
