text = input("Input: ")


def is_vowel(char):
    vowels = "aeiouAEIOU"
    return char in vowels


# new_text = ''.join(char for char in text if not is_vowel(char))
new_text = ""
for char in text:
   if not is_vowel(char):
        new_text += char


print(new_text)


