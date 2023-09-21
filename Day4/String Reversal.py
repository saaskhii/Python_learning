#Q9

var =input("Enter any number: ")
reversed_str = ""
x= len(var)-1
while x>=0:
    reversed_str +=var[x]
    x-=1
print("Reversed Number: " ,reversed_str)
