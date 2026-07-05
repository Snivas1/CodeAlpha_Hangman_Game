from game import play_game
from colorama import Fore, Style

def print_banner():
    print("\n")
    print("╔══════════════════════════════════════════════════════╗")
    print("║                                                      ║")
    print("║           🎮 CODEALPHA HANGMAN GAME 🎮              ║")
    print("║                                                      ║")
    print("║        Python Programming Internship Project         ║")
    print("║                                                      ║")
    print("╚══════════════════════════════════════════════════════╝")


def instructions():
    print("\n========== HOW TO PLAY ==========")
    print("1. Guess the hidden word one letter at a time.")
    print("2. You have only 6 incorrect attempts.")
    print("3. Each wrong guess draws the hangman.")
    print("4. Guess the complete word before the man is hanged.")
    print("5. Enter only one alphabet at a time.")
    print("=================================\n")


def choose_difficulty():

    while True:

        print("\n========== SELECT DIFFICULTY ==========")
        print("1️⃣ Easy")
        print("2️⃣ Medium")
        print("3️⃣ Hard")
        print("0️⃣ Back")
        print("=======================================")

        choice = input("Choose Difficulty: ").strip()

        if choice == "1":
            return "easy"

        elif choice == "2":
            return "medium"

        elif choice == "3":
            return "hard"

        elif choice == "0":
            return None

        else:
            print("\n❌ Invalid Choice!\n")


def menu():

    while True:

        print_banner()

        print("1️⃣ Start Game")
        print("2️⃣ Instructions")
        print("3️⃣ Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":

            level = choose_difficulty()

            if level:
                play_game(level)

        elif choice == "2":

            instructions()
            input("Press Enter to return to menu...")

        elif choice == "3":

            print("\n👋 Thank you for playing!")
            print("See you again.\n")
            break

        else:
            print("\n❌ Invalid choice. Please try again.\n")


if __name__ == "__main__":
    menu()