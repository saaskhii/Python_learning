"""7. Function Overloading: Create multiple functions with the same name but different
numbers of arguments."""

def fun(a, b=None, c=None):
    if c is not None:
        return a + b + c
    elif b is not None:
        return a + b
    else:
        return a

print(fun(1))         
print(fun(1, 2))      
print(fun(1, 2, 3))   
