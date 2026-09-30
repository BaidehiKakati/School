"""
Player module.
"""


class Player:

    def __init__(self, name=""):

        self.name = name
        self.total_score = 0

    def add_score(self, points):

        if points < 0:

            raise ValueError(
                "Points cannot be negative."
            )

        self.total_score += points