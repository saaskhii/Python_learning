#Q8

var = int(input("enter number: "))
x, y = 0, 1
count = 0

print("Fibonacci sequence:")
while count < var:
    print(x)
    z = x + y
    x = y
    y = z
    count += 1
