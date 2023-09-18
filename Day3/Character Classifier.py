#Q10
var1 = input("Enter any letter,digit or special character: ")

if var1.isalpha(): 
    print("The character ",var1," is a letter.")
elif var1.isdigit():
    print("The character ",var1," is a digit.")
else:
    print("The character ",var1," is a special character.")
