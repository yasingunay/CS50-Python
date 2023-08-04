from datetime import date
import operator
import inflect
import sys
import re

# Initialize the inflect engine
p = inflect.engine()


def main():

    # Prompt the user for their date of birth in YYYY-MM-DD format
    birth_date = input("Date of birth: ")
    try:
        year, month, day = check_birth(birth_date)
    except:
        sys.exit("Invalid date")

    date_of_birth = date(int(year), int(month), int(day))

    # Get today’s date
    date_of_today = date.today()

    # Subtract one date object from another
    result = operator.sub(date_of_today, date_of_birth)
    total_minutes = result.days * 24 * 60



    # Convert numbers to words.
    words = p.number_to_words(total_minutes, andword="")
    print(words.capitalize() + " minutes")

def check_birth(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return year, month, day


if __name__ == "__main__":
    main()