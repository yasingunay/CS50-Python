# name = input("File name: ").lower().strip()
# if name.endswith(".gif"):
#     print("image/gif")
# elif name.endswith(".jpg") or name.endswith(".jpeg"):
#     print("image/jpeg")
# elif name.endswith(".png"):
#     print("image/png")
# elif name.endswith(".txt"):
#     print("text/plain")
# elif name.endswith(".pdf"):
#     print("application/pdf")
# elif name.endswith(".zip"):
#     print("application/zip")
# else:
#     print("application/octet-stream")


name = input("File name: ").lower().strip()
extension = name.split(".")[-1]

match extension:
    case "gif":
        print("image/gif")
    case "jpg"| "jpeg":
        print("image/jpeg")
    case "png":
       print("image/png")
    case "txt":
        print("text/plain")
    case "pdf":
        print("application/pdf")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")