"""
words.py
Stores words with hints and difficulty levels.
"""

import random

WORDS = {
    "easy": [
        ("apple", "A fruit"),
        ("chair", "Furniture"),
        ("table", "Furniture"),
        ("house", "Place to live"),
        ("water", "Essential for life"),
    ],

    "medium": [
        ("python", "Programming Language"),
        ("monitor", "Computer Hardware"),
        ("network", "Connects computers"),
        ("college", "Educational Institution"),
        ("software", "Programs running on a computer"),
    ],

    "hard": [
        ("developer", "Software Professional"),
        ("algorithm", "Problem Solving Technique"),
        ("internship", "Professional Training"),
        ("artificial", "Related to AI"),
        ("programming", "Writing Computer Code"),
    ]
}


def get_random_word(level="medium"):
    """
    Returns a random word and hint
    based on difficulty level.
    """
    return random.choice(WORDS[level])