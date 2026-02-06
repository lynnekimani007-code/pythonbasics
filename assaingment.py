#a python program that allows a user enter
#a random number and checks whether
#a number is even or odd

number = int(input("Enter any number: "))
if number ==0:
    print("number is neutral")
elif number  % 2==0:
        print("The number is even.")
else:
    print("The number is odd.")