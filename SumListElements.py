#Sum of all elements in a list.
#imagine u want to count coins in ur piggy bank. 

#create a list of coins in ur piggy bank
coins = [5,10,20,5,10]

#initializing a variable to store the total
total = 0

#go through each coin and add it to the total
for coin in coins:
    total += coin
    
#printing the total amount in the sum
print("Your piggy bank has: ",total," Shillings")