def is_valid_email(email):
    return "@" in email and "." in email

def is_valid_age(age):
    return age.isdigit() and 0 < int(age) < 120

# Simulating form input
name = input("Enter your name: ").strip()
email = input("Enter your email: ").strip()
age = input("Enter your age: ").strip()

errors = []

if not name:
    errors.append("Name cannot be empty.")

if not is_valid_email(email):
    errors.append("Invalid email address.")

if not is_valid_age(age):
    errors.append("Invalid age. Must be a number between 1 and 119.")

if errors:
    print("Form submission failed due to the following errors:")
    for error in errors:
        print(f"- {error}")
else:
    print("Form submitted successfully!")

#menu selection
def show_menu():
    print("\n--- Main Menu ---")
    print("1. Add Item")
    print("2. View Items")
    print("3. Delete Item")
    print("4. Exit")

def add_item(items):
    item = input("Enter item to add: ")
    items.append(item)
    print(f"'{item}' added.")

def view_items(items):
    if not items:
        print("No items found.")
    else:
        print("Items:")
        for i, item in enumerate(items, 1):
            print(f"{i}. {item}")

def delete_item(items):
    view_items(items)
    if items:
        try:
            index = int(input("Enter item number to delete: ")) - 1
            if 0 <= index < len(items):
                removed = items.pop(index)
                print(f"'{removed}' deleted.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    items = []
    while True:
        show_menu()
        choice = input("Select an option (1-4): ")

        if choice == '1':
            add_item(items)
        elif choice == '2':
            view_items(items)
        elif choice == '3':
            delete_item(items)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

#Access control
# Define roles and permissions
permissions = {
    'admin': ['view', 'edit', 'delete'],
    'editor': ['view', 'edit'],
    'viewer': ['view']
}

# Simulate users and roles
users = {
    'alice': 'admin',
    'bob': 'editor',
    'carol': 'viewer'
}

def check_access(user, action):
    role = users.get(user)
    if not role:
        return False
    return action in permissions.get(role, [])

# Example usage
user = input("Enter your username: ")
action = input("Enter action (view/edit/delete): ")

if check_access(user, action):
    print(f"Access granted: {user} can {action}.")
else:
    print(f"Access denied: {user} cannot {action}.")

#error handling
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set_age(-5)
except ValueError as e:
    print("❌ Error:", e)
