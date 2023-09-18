#Q2

var1=input("Do you have membership (yes/no): ")
var2=float(input("Enter you purchase amount in $:"))
if var1=='yes' or var2>=150: 
    print("You are eligible for discount.")
elif var1=='no' or var2<150:
    print("You are not eligible for discount.")
else:
    print("Please enter correct input")
