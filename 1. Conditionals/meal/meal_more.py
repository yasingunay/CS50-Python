# Challenge
# If up for a challenge, optionally add support for 12-hour times, allowing the user to input times in these formats too:

#     #:## a.m. and ##:## a.m.
#     #:## p.m. and ##:## p.m.


def main():
    time = input("What time is it?: ")
    try:
        hours_and_minutes, time_indicator = time.split(" ")
    except ValueError:
        print("Invalid input. Please enter a time in the format #:## a.m. or ##:## a.m. or #:## p.m. or ##:## p.m.")
        return

    converted_time = convert(hours_and_minutes)
    if converted_time is not None:
        if (7 <= converted_time <= 8) and time_indicator == "a.m.":
            print("breakfast time")
        elif (12 <= converted_time < 13 and time_indicator == "a.m.") or (converted_time == 1 and time_indicator == "p.m."):
            print("lunch time")
        elif 6 <= converted_time <= 7 and time_indicator == "p.m.":
            print("dinner time")
        else:
            print("do not eat too much!")


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


# Other solution

# def main():
#     time = input("What time is it?: ")
#     converted_time = convert_time(time)

#     if converted_time is None:
#         print("Invalid input. Please enter a time in the format 'HH:MM a.m.' or 'HH:MM p.m.'")
#         return

#     meal_time = determine_meal_time(converted_time)
#     if meal_time is not None:
#         print(f"It's {meal_time} time!")
#     else:
#         print("It's not a mealtime. Do not eat too much!")

# def convert_time(time):
#     try:
#         hours_and_minutes, time_indicator = time.split(" ")
#         hours, minutes = map(int, hours_and_minutes.split(":"))

#         if time_indicator == "p.m." and hours != 12:
#             hours += 12
#         elif time_indicator == "a.m." and hours == 12:
#             hours = 0

#         total_hours = hours + minutes / 60
#         return total_hours
#     except (ValueError, IndexError):
#         return None

# def determine_meal_time(converted_time):
#     if 7 <= converted_time < 8:
#         return "breakfast"
#     elif 12 <= converted_time < 13:
#         return "lunch"
#     elif 18 <= converted_time < 19:
#         return "dinner"
#     else:
#         return None

# if __name__ == "__main__":
#     main()
