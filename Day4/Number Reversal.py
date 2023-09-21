#Q6

var = int(input("Enter any number: "))
reversed_num = 0
while var != 0:
    digit = var % 10
    reversed_num = reversed_num * 10 + digit
    var //= 10
print("Reversed Number: " ,reversed_num)
