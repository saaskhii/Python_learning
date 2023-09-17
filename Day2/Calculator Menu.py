#Q5
var1=float(input("Enter 1st number: "))
var2=float(input("Enter 2nd number: "))
option=['Add','Subtract','Multiply','Divide']
print("Choose any of below option")
for list in option:
    x=print(list)
var3=input("\n")
if var3=="Add":
    print("Your answer is ",var1+var2)
elif var3=="Subtract":
    print("Your answer is ",var1-var2)
elif var3=="Multiply":
    print("Your answer is ",var1*var2)
elif var3=="Divide":
    print("Your answer is ",var1/var2)
else:
    print("Please choose correct option")
