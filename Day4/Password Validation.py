#Q2

var1=input("Enter password:")
if len(var1)>=8 and any(char.isupper()for char in var1) and any(char.islower() for char in var1):
    print("Password is correct")
else:
    print("Password is not correct")
