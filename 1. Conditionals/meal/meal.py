def main():
    time = input("What time is it?: ")
    converted_time = convert(time)
    if converted_time is not None:
        if 7 <= converted_time <= 8:
            print("breakfast time")
        elif 12 <= converted_time <= 13:
            print("lunch time")
        elif 18 <= converted_time <= 19:
            print("dinner time")


def convert(time):
    try:
        hours, minutes = time.split(":")
        hours = float(hours)
        minutes = float(minutes)
        total_hours = hours + minutes / 60
        return float(total_hours)
    except ValueError:
        print("Invalid input. Please enter a time in the format 'HH:MM'.")
        return None


if __name__ == "__main__":
    main()