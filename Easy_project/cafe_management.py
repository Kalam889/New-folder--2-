menu = {"coffee":80,
        "burger":150,
        "sandwich":100,
        "momo":70
        }
bill = []
while True:
    order = input("Enter your order: ").lower()
    if order not in menu:
        print(f"{order} is not in our menu.")
    else:
        bill.append(menu[order])
        print(f"{order} has been added in order list.")
        print(f"The price of your {order} is {menu[order]}")
    order_2 = input("Would you like to order something else ?(yes/no)").lower()
    if order_2 == "no":
        break
    elif order_2 == "yes":
        order = input("Enter your order: ").lower()
        if order not in menu:
            print(f"{order} is not in our menu.")
        else:
            print(f"{order} has been added in order list.")
            print(f"The price of your {order} is {menu[order]}")
            bill.append(menu[order])
    else:
        print("Invalid input")
        break
total_bill = sum(bill)
print(f"\nYour total bill is ₹{total_bill}")
