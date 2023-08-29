from datetime import datetime

while True:
    try:
        date_input = input("Date: ").strip()
        date = datetime.strptime(date_input, "%m/%d/%Y")
    except ValueError:
        try:
            date = datetime.strptime(date_input, "%B %d, %Y")
        except ValueError:
            continue
        else:
            print(f"{date.year}-{date.month:02}-{date.day:02}")
            break

    else:
        print(f"{date.year}-{date.month:02}-{date.day:02}")
        break






# Other solution

# from datetime import datetime

# def parse_date(date_input):
#     formats_to_try = ["%m/%d/%Y", "%B %d, %Y"]

#     for date_format in formats_to_try:
#         try:
#             date = datetime.strptime(date_input, date_format)
#             return date.strftime("%Y-%m-%d")
#         except ValueError:
#             pass

#     return None

# while True:
#     date_input = input("Date: ").strip()
#     formatted_date = parse_date(date_input)

#     if formatted_date:
#         print(formatted_date)
#         break

