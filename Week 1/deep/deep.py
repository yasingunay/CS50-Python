input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
if input == "42":
    print("Yes")
elif input == "forty-two":
    print("Yes")
elif input == "forty two":
    print("Yes")
else:
    print("No")
