while True:
    try:
        x,y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        if x > y:
            continue
        percentage = x / y * 100
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{round(percentage)}%")


# Other solution

# def get_fraction():
#     while True:
#         try:
#             x, y = input("Enter a fraction (x/y): ").split("/")
#             x = int(x)
#             y = int(y)
#             if y == 0:
#                 continue
#             if x > y:
#                 continue
#         except ValueError:
#             continue
#         else:
#             return x, y

# def calculate_percentage(x, y):
#     percentage = x / y * 100
#     return percentage

# x, y = get_fraction()
# percentage = calculate_percentage(x, y)

# if percentage <= 1:
#     print("E")
# elif percentage >= 99:
#     print("F")
# else:
#     print(f"{round(percentage)}%")
