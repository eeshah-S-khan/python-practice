#If the number is 0 or 1, just return 1, this stops the recursion.
#Otherwise, multiply the number by the factorial of the number before it (n-1).
#The function keeps calling itself until it reaches 1, then multiplies all the results on the way back up.

#defining a function to calculate the factorial recursively
def factorial(n):
    if n==0 or n==1:
        return 1
    else: 
        return n * factorial(n-1)

# ask the user for a number 
num = int(input("Enter a number: "))

#call the functio and print the result 
print("Factorial of ", num, "is", factorial(num))
