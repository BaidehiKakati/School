"""
Scoreboard module.

Stores game results during
the current game session.
"""


class ScoreBoard:

    def __init__(self):

        self.records = []

    def add_record(
        self,
        name,
        mode,
        score,
        attempts
    ):

        record = {

            "name": name,

            "mode": mode,

            "score": score,

            "attempts": attempts
        }

        self.records.append(record)

    def get_records(self):

        return sorted(
            self.records,
            key=lambda record: record["score"],
            reverse=True
        )