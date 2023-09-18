#Q9
age=int(input("Enter your agr:"))
id=input("Do you have student ID (yes/No):")
if age==4 or age<=10:
    print("You are minor")
    if age<4 and id=="yes":
        print("you cannot have student id")
    elif id=="yes":
        print("Your fare is 200")
    elif id=="no":
        print("your fare is 500")
elif age>10 and id=="yes":
    print("your fare is 1000")
elif age>10 and id=="no":
    print("your fare is 1500")
else:
    print("enter valid age")
