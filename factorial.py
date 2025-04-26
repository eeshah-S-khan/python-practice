#ask the user for a number 
n = int(input("Enter a number: "))

#initialize the result
factorial = 1

#creating a variable to control the loop.
i = 1

#using a while loop to calculate the factorial 
while i <= n:
    factorial *= i
    i += 1
    
#printing the result 
print("factorial of ",n," is", factorial)