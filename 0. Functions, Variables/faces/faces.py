def main():
    str = input()
    converted_str = convert(str)
    print(converted_str)

def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str

main()