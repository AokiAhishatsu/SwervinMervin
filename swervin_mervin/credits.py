class Credits:
    """Plays the credits sequence at the end of the game."""

    def __init__(self):
        self.finished = False
 
    def progress(self, window):
        self.finished = True
