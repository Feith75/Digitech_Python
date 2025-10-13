#We are perfoming the  for loop
for number in range(0,10):
    print(number)
    
    for number in range(10):
        print(number*"#")
#even number
        for number in range(10):
            if number%2 ==0:
                print(number)
     #old number
                for number in range(10):
                    if number %2==1:
                        print(number)
#we are perfoming the while loop
trial = 3
attempt = 0
 
while attempt < trial:
    value=input("Enter the password")
    if value == "faith123":
        print("log in succeddfully")
    else:
        print("the password is wrong try again!!")
        attempt+=1
else :
    print("you've failed number of attempts are over")
