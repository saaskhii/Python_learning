#Q3

a="sakshi"
x=3
while x>0:
    var1=input("Enter password:")
    if a==var1:
        print("Password is correct")
        break
    else:
        print("Password is not correct")
        x-=1
        
if x==0:
    print("attempt over")
