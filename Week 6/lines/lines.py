import sys


def main():
    if len(sys.argv) <= 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        lines = check_and_read_file()
        line_count = count_lines(lines)
        print(line_count)


def check_and_read_file():
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        try:
            with open(sys.argv[1], "r") as file:
                return file.readlines()
        except FileNotFoundError:
            sys.exit("File does not exist")


def count_lines(lines):
    line_count = 0
    for line in lines:
        # Remove leading and trailing whitespace
        line = line.strip()

        # Ignore empty lines and comment lines
        if line and not line.startswith("#"):
            line_count += 1
    return line_count


if __name__ == "__main__":
    main()
