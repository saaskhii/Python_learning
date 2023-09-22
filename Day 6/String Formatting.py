#Q9
x=input("Enter any phone no: ")
if len(x)==10:
    print("{}-{}-{}".format(x[:3], x[3:6],x[6:]))
else:
    print("enter correct number")
