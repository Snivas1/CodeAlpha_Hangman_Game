from colorama import Fore, Style, init
from hangman_art import get_hangman_stage

# Initialize colorama
init(autoreset=True)
def display_game(word, hint, guessed_letters, attempts):

    print("\n" + Fore.CYAN + "=" * 55)
    print(Fore.BLUE + Style.BRIGHT + "           🎮 CODEALPHA HANGMAN GAME 🎮")
    print(Fore.CYAN + "=" * 55)

    print(Fore.YELLOW + get_hangman_stage(attempts))

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += Fore.GREEN + letter.upper() + " "
        else:
            display_word += Fore.WHITE + "_ "

    hearts = "❤️ " * attempts

    print(Fore.MAGENTA + f"\n💡 Hint            : {hint}")
    print(Fore.CYAN + f"🔤 Word            : {display_word}")
    print(Fore.RED + f"❤️ Lives           : {hearts}")

    if guessed_letters:
        print(Fore.YELLOW + "📝 Guessed Letters :", " ".join(sorted(guessed_letters)))
    else:
        print(Fore.YELLOW + "📝 Guessed Letters : None")

    print(Fore.CYAN + "=" * 55)

def is_valid_guess(guess, guessed_letters):

    if len(guess) != 1:
        return False, Fore.YELLOW + "⚠ Please enter only ONE letter."

    if not guess.isalpha():
        return False, Fore.YELLOW + "⚠ Enter alphabet letters only."

    if guess in guessed_letters:
        return False, Fore.YELLOW + "⚠ Letter already guessed."

    return True, ""