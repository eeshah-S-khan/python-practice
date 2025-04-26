#if a number divided by 2, leaves no remainder -- it is even
#if there is a remainder -- it is odd

#ask the user to input a number
number = int(input("Input a number: "))

#check if the number is odd or even
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd")