import random
import sys


def main():
    n = get_level()
    random_nb = random.randint(1, n)
    get_guess_and_compare(random_nb)


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                return n
        except ValueError:
            pass


def get_guess_and_compare(random_nb):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 0:
                continue
            elif guess < random_nb:
                print("Too small!")
            elif guess > random_nb:
                print("Too large!")
            else:
                print("Just right!")
                sys.exit()
        except ValueError:
            pass


if __name__ == "__main__":
    main()
