def main():
    text = input("camelCase: ")
    new_text = ""
    for char in text:
        if char.isupper():
            new_text += "_" + char.lower()
        else:
            new_text += char

    print(new_text)


if __name__ == "__main__":
    main()

# You can also use replace() funtion