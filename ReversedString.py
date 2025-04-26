# ask the user for a string 
text = input("Enter a string: ")

# we are going to start with an empty reversed_text
# for every character in text, add it to the beginning of the reversed_text

#initializing an empty string to store the reversed string
reversed_string = ""

#use a for loop to go through each character in the text
for char in text:
    reversed_string = char + reversed_string
    
#print the reversed string
print("Reversed string: ", reversed_string)