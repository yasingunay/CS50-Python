def main():
    grocery_list={}
    populate_grocery_lis(grocery_list)
    list_items(grocery_list)


def populate_grocery_lis(grocery_dict):
    while True:
        count = 1
        try:
            item = input().lower()
            if item not in grocery_dict:
                grocery_dict[item] = count
            else:
                count = grocery_dict.get(item)
                count += 1
                grocery_dict[item] = count

        except EOFError:
            break


def list_items(grocery_dict):
    for key,value in sorted(grocery_dict.items()):
        print(f"{value} {key.upper()}")


main()


