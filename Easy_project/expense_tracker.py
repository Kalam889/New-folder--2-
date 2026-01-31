expenses = []
while True:
    name = input("Enter expense name: ").strip()
    if name.lower() == "exit":
        break
    amount = float(input("Enter expense amount: "))
    category = input("Enter category: ").strip().capitalize()
    expenses.append({"Name": name, "Amount": amount, "Category": category})
print("\nAll expenses: ")
for e in expenses:
    print(f"{e['Name']} - ₹{e['Amount']} ({e['Category']})")