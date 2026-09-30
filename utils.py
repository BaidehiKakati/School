"""
Utility functions for CodeQuest.
"""

import os


def get_int(
    prompt,
    minimum,
    maximum
):

    while True:

        try:

            value = int(
                input(prompt)
            )

            if (
                minimum
                <= value
                <= maximum
            ):

                return value

            print(
                f"Please enter a number "
                f"between {minimum} and {maximum}."
            )

        except ValueError:

            print(
                "Invalid input!"
            )

            print(
                "Please enter a whole number."
            )


def pause():

    input(
        "\nPress Enter to continue..."
    )


def clear_screen():

    os.system(
        "cls"
        if os.name == "nt"
        else "clear"
    )