import csv
import sys


def main():
    # Check command-line arguments
    if len(sys.argv) <= 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        students = read_file(sys.argv[1])
        new_list = create_new_list(students)
        write_data_to_output(new_list, sys.argv[2])


# Function to read input file
def read_file(input_file):
    students = []
    try:
        with open(input_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

    return students


# Function to create a new student list by splitting each name into a first name and last name.
def create_new_list(students):
    new_list = []
    for student in students:
        # Split each name into a first name and last name.
        last_name, first_name = student["name"].split(",")
        new_list.append(
            {
                "first": first_name.strip(),
                "last": last_name.strip(),
                "house": student["house"],
            }
        )
    return new_list


# Function to write new student list to output file
def write_data_to_output(new_list, output_file):
    try:
        # Open outpile file in write mode
        with open(output_file, "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            # Write fieldnames to a file using writeheader
            writer.writeheader()
            for line in new_list:
                writer.writerow(line)
    except FileNotFoundError:
        sys.exit(f"Could not write to {output_file}")


if __name__ == "__main__":
    main()
