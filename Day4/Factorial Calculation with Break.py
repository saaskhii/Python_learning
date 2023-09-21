#Q8

var = int(input("Enter a number: "))
fact = 1
x = 1
while True:
    fact *= x
    x += 1

    if fact > 1000000:
        print("Factorial result is too large. Stopping calculation.")
        break
    if x > var:
        break
print(f"The factorial is:" ,fact)
