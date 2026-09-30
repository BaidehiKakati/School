"""
Main game controller for Guess the Number.
"""

from random import randint
from player import Player
from scoreboard import ScoreBoard
from utils import get_int, pause, clear_screen


class GuessTheNumberGame:

    def __init__(self):
        self.player = Player()
        self.scoreboard = ScoreBoard()

    def start(self):

        self.show_title()

        self.show_rules()

        self.player.name = input(
            "\nEnter your name: "
        ).strip()

        if self.player.name == "":
            self.player.name = "Player"

        while True:

            clear_screen()

            self.show_title()

            print(f"Player:{self.player.name}")
            print(f"Total Score:{self.player.total_score}")

            print("\n" + "=" * 40)
            print("             MAIN MENU")
            print("=" * 40)

            print("\n1.Easy Mode")
            print("2.Medium Mode")
            print("3.Hard Mode")
            print("4.Scoreboard")
            print("5.Rules")
            print("6.Exit")

            choice = get_int(
                "\nChoose an option: ",
                1,
                6
            )

            if choice == 1:

                self.play_round(
                    "Easy",
                    1,
                    50,
                    6,
                    20
                )

            elif choice == 2:

                self.play_round(
                    "Medium",
                    1,
                    100,
                    7,
                    20
                )

            elif choice == 3:

                self.play_round(
                    "Hard",
                    1,
                    500,
                    8,
                    40
                )

            elif choice == 4:

                self.show_scoreboard()

            elif choice == 5:

                self.show_rules()

            elif choice == 6:

                print("\n" + "=" * 50)
                print("          THANK YOU FOR PLAYING!")
                print("=" * 50)

                print(
                    f"\nFinal Score: "
                    f"{self.player.total_score}"
                )

                break

    def show_title(self):

        print("\n" + "=" * 60)

        print(
            "             GUESS THE NUMBER"
        )

        print(
            "          PYTHON NUMBER CHALLENGE"
        )

        print("=" * 60)

    def show_rules(self):

        print("\n" + "=" * 60)
        print("        RULES")
        print("=" * 60)

        print("""
1.The objective of the game is for the player to guess the secret number within a limited number of attempts.
2.The player can choose from three difficulty levels: Easy, Medium, and Hard.
3.Each difficulty level has a different range of numbers and a different number of attempts.
4.Easy Mode: The player has to guess a number between 1 to 50.
5.Medium Mode: The player has to guess a number between 1 to 100.
6.Hard Mode: The player has to guess a number between 1 to 500.
7.After each guess, a hint will be given to the player indicating whether your guess was too high, too low, or correct.
8.Correct answer gives points to the player.
9.The player gets more points for guessing the number in fewer attempts.
10.The player can view the scoreboard to see their total score and compare it with other players. 
""")

        print("=" * 60)

        pause()

    def play_round(
        self,
        mode,
        low,
        high,
        attempts,
        base_score
    ):

        clear_screen()

        self.show_title()

        secret_number = randint(low, high)

        print(f"\n     {mode.upper()} MODE")

        print(
            f"\nGuess a number between "
            f"{low} and {high}."
        )

        print(
            f"You have {attempts} attempts to guess the number."
        )

        for attempt in range(
            1,
            attempts + 1
        ):

            guess = get_int(
                f"\nAttempt {attempt}/{attempts}: ",
                low,
                high
            )

            if guess == secret_number:

                points = (
                    base_score + (attempts - attempt) * 5
                )

                self.player.add_score(points)

                self.scoreboard.add_record(
                    self.player.name,
                    mode,
                    points,
                    attempt
                )

                print("\n" + "=" * 50)

                print("         CORRECT Guess!")

                print("=" * 50)

                print(
                    f"\nThe secret number was "
                    f"{secret_number}."
                )

                print(f"\n You guessed it in {attempt} attempts.")

                print(
                    f"You earned "
                    f"{points} points!"
                )

                print(
                    f"Total Score: "
                    f"{self.player.total_score}"
                )

                pause()

                return

            if guess < secret_number:

                print(
                    "Hint: Your guess is too low than the secret number. "
                    "Guess is HIGHER."
                )

            else:

                print(
                    "Hint: Your guess is too high than the secret number. "
                    "Guess is LOWER."
                )

        self.scoreboard.add_record(
            self.player.name,
            mode,
            0,
            attempts
        )

        print("\n" + "=" * 50)

        print("         GAME OVER")

        print("=" * 50)

        print(
            f"\nThe secret number was "
            f"{secret_number}."
        )

        print("You earned 0 points.")

        pause()

    def show_scoreboard(self):

        clear_screen()

        self.show_title()

        print("\n" + "=" * 60)
        print("                    SCOREBOARD")
        print("=" * 60)

        records = self.scoreboard.get_records()

        if not records:

            print("\nNo games have been played yet. Start playing to see your scores here!")

        else:

            print()

            for index, record in enumerate(
                records,
                1
            ):

                print(
                    f"{index}. "
                    f"{record['name']} | "
                    f"{record['mode']} | "
                    f"{record['score']} points | "
                    f"{record['attempts']} attempts"
                )

        print(
            f"\nCurrent Total Score: "
            f"{self.player.total_score}"
        )

        pause()