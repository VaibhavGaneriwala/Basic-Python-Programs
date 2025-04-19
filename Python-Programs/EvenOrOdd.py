"""
Author: Vaibhav Ganeriwala
Date: 2025-04-19
Description: This script checks if a given number is even or odd.
"""

def is_even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

if __name__ == "__main__":
    try:
        number = int(input("Enter a number to check if it's even or odd: "))
        print(f"The number {number} is {is_even_or_odd(number)}.")
    except ValueError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")