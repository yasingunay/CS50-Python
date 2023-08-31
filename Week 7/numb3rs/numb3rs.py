# import re
# import sys


# PATTERN = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

# # 25[0-5]: Matches numbers from 250 to 255.
# # 2[0-4][0-9]: Matches numbers from 200 to 249.
# # [01]?[0-9][0-9]?: Matches numbers from 0 to 199.


# def main():
#     print(validate(input("IPv4 Address: ")))


# def validate(ip):
#     if re.search(PATTERN, ip.strip()):
#         return True
#     else:
#         return False


# if __name__ == "__main__":
#     main()


# Other solution

# import re
# import sys


# def main():
#     print(validate(input("IPv4 Address: ")))


# def validate(ip):
#     try:
#         bytes = ip.strip().split(".")
#         if len(bytes) != 4:
#             return False
#         for byte in bytes:
#             byte = int(byte)
#             if byte not in range(256):
#                 return False
#         return True
#     except ValueError:
#         return False


# if __name__ == "__main__":
#     main()


# # Other solution 2

# import re
# import sys


# def main():
#     print(validate(input("IPv4 Address: ")))


# def validate(ip):
#     try:
#         bytes = ip.strip().split(".")
#         if len(bytes) != 4:
#             return False
#         for byte in bytes:
#             if not re.search(r"^1?[0-9][0-9]?$|2[0-4][0-9]|25[0-5]", byte):
#                 return False
#         return True
#     except ValueError:
#         return False


# if __name__ == "__main__":
#     main()
