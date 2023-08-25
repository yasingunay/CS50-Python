amount_due = 50
while True:
    print(f"Amount Due: {amount_due}")
    insert_coin = int(input("Insert Coin: "))
    if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
        if amount_due < insert_coin:
            change_owed = insert_coin - amount_due
            print(f"Change Owed: {change_owed}")
            break
        else:
            amount_due -=insert_coin
            if amount_due == 0:
                print("Change Owed: 0")
                break
            else:
                continue
    