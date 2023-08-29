import random


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    score = 0
    level_ranges = {1: (0, 9), 2: (10, 99), 3: (100, 999)}
    min_range, max_range = level_ranges[level]
    for _ in range(10):
        x = random.randint(min_range, max_range)
        y = random.randint(min_range, max_range)
        result = x + y
        print(f"{x} + {y} = ", end="")
        three_tries = 3

        while three_tries > 0:
            try:
                guess = int(input())  # Wait for user input
            except ValueError:
                print("EEE")
                three_tries -= 1
                print(f"{x} + {y} = ", end="")
            else:
                if guess != result:
                    print("EEE")
                    three_tries -= 1
                    print(f"{x} + {y} = ", end="")
                    if three_tries == 0:
                        print(f"{result}")
                else:
                    score += 1
                    break

    print(f"Score: {score}")


if __name__ == "__main__":
    main()
