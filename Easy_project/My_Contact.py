contacts = {}
while True:
    print("\nContact Book")
    print("1.Add to contact")
    print("2.Search contact")
    print("3.Update contact")
    print("4.Delete contact")
    print("5.Exit")
    choice = input("Click your choice:")
    if choice == "1":
        Name = input("Enter name: ")
        Number = input("Enter number: ")
        Email = input("Enter email: ")
        contacts[Name] = {"Number": Number, "Email": Email}
        print(f"{Name} has been saved.")
    elif choice == "2":
        search_contact = input("Enter name:")
        if search_contact in contacts:
            print(f"Phone:{contacts[search_contact]['Number']}")
            print(f"Email:{contacts[search_contact]['Email']}")
          
        else:
            print("Contact does not exist.")
    elif choice == "3":
        update_name = input("Enter name: ")
        if update_name in contacts:
            update_number = input("Enter number: ")
            update_mail = input ("Enter mail: ")
            contacts[update_name] = {"Number": update_number, "Email": update_mail}
            print(f"{update_name} has been deleted successfully.")
        else:
            print("Contact does not exist.")
    elif choice == "4":
        delete_name = input("Enter name: ")
        if delete_name in contacts:
            del contacts[delete_name] 
            print(f"{delete_name} has been deleted successfully.")
        else:
            print(f"{delete_name} does not exist.")
    elif choice == "5":
        print("Good bye!")
        break