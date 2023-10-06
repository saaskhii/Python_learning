""" Conditional Return: Create a function that returns "Even" if a given number is even
and "Odd" if it's odd."""

def fun(n):
    
    if n%2==0:
        return f"{n} is Even."
    else:
        return f"{n} is Odd."
    
a=int(input("Enter number: "))
res=fun(a)
print(res)
