# % - modulus operator will give the remainder(last digit)
# // - floor division, removes the decimal part and keeps the whole number

#ask the user for a number 
num = int(input("Enter a number: "))

#initializing a variable to store the sum
sum = 0

while num != 0:
    last_digit = num % 10 # gets the last digit
    sum += last_digit #adds last digit to the sum
    num = num // 10 #gets rid of the last digit
    
#print the final sum
print("Sum of digits: ", sum)