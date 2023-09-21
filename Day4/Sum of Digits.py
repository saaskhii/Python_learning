#Q4

var=int(input("Enter a number:"))
x=0
while(var>0):
    sum=var%10
    x=x+sum
    var=var//10
print("The total sum of digits is:",x)

