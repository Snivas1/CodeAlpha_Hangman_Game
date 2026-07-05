from colorama import Fore
from words import get_random_word
from utils import display_game, is_valid_guess


def play_game(level):
    """Main game loop."""

    word, hint = get_random_word(level)

    guessed_letters = []
    attempts = 6

    while attempts > 0:

        display_game(
            word=word,
            hint=hint,
            guessed_letters=guessed_letters,
            attempts=attempts
        )

        guess = input("\nEnter a letter: ").lower().strip()

        valid, message = is_valid_guess(guess, guessed_letters)

        if not valid:
            print(message)
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(Fore.GREEN + "\n✅ Correct Guess!")
        else:
            attempts -= 1
            print(Fore.RED + "\n❌ Wrong Guess!")

        if all(letter in guessed_letters for letter in word):

            display_game(
                word=word,
                hint=hint,
                guessed_letters=guessed_letters,
                attempts=attempts
            )

            print(Fore.GREEN + "\n🏆 CONGRATULATIONS!")
            print(Fore.GREEN + f"🎯 You guessed: {word.upper()}")

            return True

    display_game(
        word=word,
        hint=hint,
        guessed_letters=guessed_letters,
        attempts=attempts
    )

    print(Fore.RED + "\n💀 GAME OVER!")
    print(Fore.YELLOW + f"The correct word was: {word.upper()}")

    return False