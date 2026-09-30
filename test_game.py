"""
Unit tests for CodeQuest.

Run using:

python -m unittest test_game.py
"""

import unittest

from player import Player
from scoreboard import ScoreBoard


class TestPlayer(unittest.TestCase):

    def test_add_score(self):

        player = Player("Test")

        player.add_score(20)

        self.assertEqual(
            player.total_score,
            20
        )

    def test_multiple_scores(self):

        player = Player("Test")

        player.add_score(10)

        player.add_score(30)

        self.assertEqual(
            player.total_score,
            40
        )

    def test_negative_score(self):

        player = Player("Test")

        with self.assertRaises(ValueError):

            player.add_score(-5)


class TestScoreBoard(unittest.TestCase):

    def test_add_record(self):

        board = ScoreBoard()

        board.add_record(
            "Test",
            "Easy",
            30,
            2
        )

        records = board.get_records()

        self.assertEqual(
            len(records),
            1
        )

        self.assertEqual(
            records[0]["score"],
            30
        )

    def test_score_sorting(self):

        board = ScoreBoard()

        board.add_record(
            "Player1",
            "Easy",
            10,
            5
        )

        board.add_record(
            "Player2",
            "Hard",
            50,
            2
        )

        records = board.get_records()

        self.assertEqual(
            records[0]["score"],
            50
        )


if __name__ == "__main__":

    unittest.main()