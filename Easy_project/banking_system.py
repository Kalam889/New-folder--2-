balance = 0
while True:

    print("1.Deposit: ")
    print("2.Withdraw: ")
    print("3.Balance: ")
    print("4.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
   
        deposit_amount = float(input("Enter amount to deposit: "))
        if deposit_amount < 0:
            print("Amount should be more than 0.")
        else:
            balance += deposit_amount
            print(f"Your deposite amount is Rs.{deposit_amount}")
         

    elif choice == "2":
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount < 0 :
            print("Your amount should be greater than 0")
        else:
            balance -= withdraw_amount  
            print(f"Your withdrawl amount is Rs.{withdraw_amount}")
    
    elif choice == "3":
        print(f"Your available balance is Rs.{balance}")

    elif choice == "4":
        print("Goodbye! Have a good day")
        break
    else:
        print("Invalid choice")