import random
WIDTH = 70

def top_border():
    print("=" * WIDTH)


def middle_border():
    print("-" * WIDTH)


def bottom_border():
    print("=" * WIDTH)


def show_header():
    print()
    top_border()
    print("🎯 NUMBER GUESSING GAME".center(WIDTH))
    bottom_border()


def guessing_game():

    secret_number = random.randint(1, 100)
    attempts = 0

    show_header()

    print()
    top_border()
    print("I have selected a number between 1 and 100.".center(WIDTH))
    print("Try to guess the correct number!".center(WIDTH))
    bottom_border()

    while True:

        try:
            guess = int(input("\n👉 Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("\n⚠️ Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:

                print()
                top_border()
                print("📉 TOO LOW!".center(WIDTH))
                print("Try a higher number.".center(WIDTH))
                bottom_border()

            elif guess > secret_number:

                print()
                top_border()
                print("📈 TOO HIGH!".center(WIDTH))
                print("Try a lower number.".center(WIDTH))
                bottom_border()

            else:

                print()
                top_border()
                print("🎉 CORRECT GUESS!".center(WIDTH))
                print(f"The number was {secret_number}.".center(WIDTH))
                print(f"Attempts: {attempts}".center(WIDTH))
                print("🏆 Congratulations!".center(WIDTH))
                bottom_border()

                break

        except ValueError:

            print()
            top_border()
            print("❌ INVALID INPUT".center(WIDTH))
            print("Please enter numbers only.".center(WIDTH))
            bottom_border()

guessing_game()