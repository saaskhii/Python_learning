#Q8
var1=float(input("Enter side 1 of triangle:"))
var2=float(input("Enter side 2 of triangle:"))
var3=float(input("Enter side 3 of triangle:"))
if var1==var2==var3:
    print("equilateral")
elif var1==var2 or var1==var3 or var2==var3:
    print("isosceles")
else:
    print("scalene")
