import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe.+></iframe>", s):
        if match := re.search(
            r"(?:http)s?://(?:www.)?youtube\.com/embed/([a-zA-Z0-9]+)", s.strip()
        ):
            video_id = match.group(1)
            return f"https://youtu.be/{video_id}"


if __name__ == "__main__":
    main()
