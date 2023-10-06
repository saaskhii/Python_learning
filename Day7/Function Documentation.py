#q6

def fact():
    """
    Calculate the factorial of a given number.
    Prompts the user to input a number and calculates its factorial using a for loop. The factorial of a non-negative integer n is the product of all positive integers from 1 to n.

    Example:
        Input: 5
        Output: Factorial of 5 is: 120
    """
    var = int(input("Enter number: "))
    n = 1
    for x in range(1, var + 1):
        n *= x
    
    print( x)
fact()
