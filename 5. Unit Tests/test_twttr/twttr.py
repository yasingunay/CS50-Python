def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for char in word:
        if char in vowels:
            word = word.replace(char, "")
    return word


if __name__ == "__main__":
    main()
