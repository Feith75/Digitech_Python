name = input("Enter your name: ")
email = input("Enter your email: ")
age = input("Enter your age: ")

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

