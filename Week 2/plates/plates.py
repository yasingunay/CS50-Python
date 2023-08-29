def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (is_start_with_at_least_two_letter(s)
        and check_len(s)
        and is_alpha_or_is_digit(s)
        and check_first_number(s)
        and check_numbers(s)
    )


# “All vanity plates must start with at least two letters.”
def is_start_with_at_least_two_letter(s):
    return s[0:2].isalpha()

# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def check_len(s):
    return 2 <= len(s) <= 6

# The first number used cannot be a ‘0’.”
def check_first_number(s):
    for i in range(len(s) -1):
        if s[i].isalpha():
            if s[i + 1] == '0':
                return False
    return True

# “Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
def check_numbers(s):
    for i in range(len(s) - 1):
        if s[i].isdigit():
            if not s[i + 1].isdigit():
                return False
    return True


# “No periods, spaces, or punctuation marks are allowed.”
def is_alpha_or_is_digit(s):
    for char in s:
        if not (char.isalpha() or char.isdigit()):
            return False
    return True

    # return all(char.isalpha() or char.isdigit() for char in s)

main()