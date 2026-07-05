"""
hangman_art.py
Contains all Hangman ASCII art.
"""

HANGMAN_PICS = [
    r"""
 +---+
 |   |
     |
     |
     |
     |
=========
""",
    r"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",
    r"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",
    r"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",
    r"""
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========
""",
    r"""
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========
""",
    r"""
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
"""
]


def get_hangman_stage(attempts_left):
    return HANGMAN_PICS[6 - attempts_left]