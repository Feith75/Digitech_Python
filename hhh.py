menu = True

while menu:
    print("\n--- Main Menu ---")
    print("1. view items")
    print("2. select")
    print("3. buy")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("items...")
    elif choice == "2":
        print("selected items...")
    elif choice == "3":
        print("bought...")
    elif choice == "4":
        print("Exiting... Goodbye!")
        menu= False
    else:
        print("Invalid selection. Please try again.")
    
print("Invalid input.Please enter a number(1-4)")