#Q6

var1=float(input("Enter your score:"))
if var1>85:
    print("You have score A grade")
elif var1>=65 and var1<=85:
    print("You have score B grade")
elif var1>=50 and var1<65:
    print("You have score C grade")
elif var1>=35 and var1<50:
    print("You have score D grade")
else:
    print("You have score F grade")
