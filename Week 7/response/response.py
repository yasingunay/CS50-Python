from validator_collection import validators, errors


def main():
    email = input("What's your email address? ")
    if check_email(email):
        print("Valid")
    else:
        print("Invalid")


def check_email(email):
    try:
        email = validators.email(email, allow_empty=False)
        return True
    except errors.InvalidEmailError:
        return False
    except ValueError:
        return False


if __name__ == "__main__":
    main()
