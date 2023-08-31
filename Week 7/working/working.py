import re
import sys

# Function to convert time ranges
def main():
    print(convert(input("Hours: ")))

# Convert function to handle different time formats
def convert(time_str):
    # Convert input to uppercase for consistent matching
    time_str = time_str.upper()

    # Check if the time string matches the first format (with minutes)
    if re.match(
        r"^(\d?\d):([0-5][0-9]) ([AP][M]) TO (\d?\d):([0-5][0-9]) ([AP][M])$",
        time_str,
        re.IGNORECASE,
    ):
        # Extract matched groups
        match = re.search(
            r"^(\d?\d):([0-5][0-9]) ([AP][M]) TO (\d?\d):([0-5][0-9]) ([AP][M])$",
            time_str,
            re.IGNORECASE,
        )
        (
            start_hour,
            start_minute,
            start_meridiem,
            end_hour,
            end_minute,
            end_meridiem,
        ) = map(match.group, [1, 2, 3, 4, 5, 6])
        start_hour, end_hour = int(start_hour), int(end_hour)

        # Convert hours based on meridiem (AM/PM)
        if start_meridiem == "PM" and start_hour < 12:
            start_hour += 12
        elif start_meridiem == "AM" and start_hour == 12:
            start_hour = 0

        if end_meridiem == "PM" and end_hour < 12:
            end_hour += 12
        elif end_meridiem == "AM" and end_hour == 12:
            end_hour = 0

        return f"{start_hour:02}:{start_minute} to {end_hour:02}:{end_minute}"

    # Check if the time string matches the second format (without minutes)
    elif re.match(r"^(\d?\d) (AM|PM) TO (\d?\d) (AM|PM)$", time_str, re.IGNORECASE):
        match = re.search(
            r"^(\d?\d) (AM|PM) TO (\d?\d) (AM|PM)$", time_str, re.IGNORECASE
        )
        start_hour, start_meridiem, end_hour, end_meridiem = map(
            match.group, [1, 2, 3, 4]
        )
        start_hour, end_hour = int(start_hour), int(end_hour)

        # Convert hours based on meridiem (AM/PM)
        if start_meridiem == "PM" and start_hour < 12:
            start_hour += 12
        elif start_meridiem == "AM" and start_hour == 12:
            start_hour = 0

        if end_meridiem == "PM" and end_hour < 12:
            end_hour += 12
        elif end_meridiem == "AM" and end_hour == 12:
            end_hour = 0

        return f"{start_hour:02}:00 to {end_hour:02}:00"

    # If neither format matches, raise an error
    else:
        raise ValueError("Invalid time format")

# Entry point of the script
if __name__ == "__main__":
    main()
