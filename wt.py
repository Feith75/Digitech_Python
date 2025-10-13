permissions = {
    'admin': ['view', 'edit', 'delete'],
    'editor': ['view', 'edit'],
    'viewer': ['view']
}
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
