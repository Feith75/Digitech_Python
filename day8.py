#how we can define a function in python.
#def get_pass(name, age):
   # if age <=17:
       # return f"{name},you are not allowed to go in"
    #else:
        #return f"{name},you are allowed to go in!!"
    
#generate the actual name and age
#user_name = input("Enter your name: ")
#user_age = int(input("Enter your age: "))
    
#final = get_pass(user_name, user_age)
#print(final)

def get_access():
 try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if age <=17:
        print(f"{name},you are not allowed to go in")
    else:
        print (f"{name},you are allowed to go in!!")
 except ValueError:
    print("weka namba usieke maneno")
 finally:
    print("Thank you for using our services")

get_access()
