import sys
import csv
from tabulate import tabulate


def main():
    # Check command-line argument is valid. If not exit the program
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        menu = read_file(sys.argv[1])
        # Take the first_line as a header
        first_row = menu[0]
        # Do not print first line(headers) again with Slicing
        print(tabulate(menu[1:], headers=first_row, tablefmt="grid"))


def read_file(file):
    menu = []
    try:
        with open(file) as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                menu.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist!")
    return menu


if __name__ == "__main__":
    main()
