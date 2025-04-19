"""
Author: Vaibhav Ganeriwala
Date: 2025-04-19
Description: This script calculates the factorial of a given number using recursion.
"""

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
if __name__ == "__main__":
    try:
        number = int(input("Enter a number to calculate its factorial: "))
        result = factorial(number)
        print(f"The factorial of {number} is {result}.")
    except ValueError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")