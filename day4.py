#login validation
#this program checks on the user input and validat it

print("This programe needs the credentials to verify them to give grant access to users")
print()

username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "faith"and password == "faith123":
    print("signed in successful")
elif username != "faith" and password == "faith123":
    print("check your credentials and try again!!")
else:
    print("wrong credentials")