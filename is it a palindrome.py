# Function
def string(string):
    
    # Reversing the string
    stringr = string[::-1]
    
    # Checking if its a palindrome
    if stringr == string:
        print("it is a palindrome")
        
    else:
        print("it is not a palindrome")

string(input("Type Something To See if its A Palindrome: "))
