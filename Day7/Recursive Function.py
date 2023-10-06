#q10

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

a = int(input("enter number: "))
result = fib(a)
print(f"The {a}th Fibonacci number is: {result}")
