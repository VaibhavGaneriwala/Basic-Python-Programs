"""
Author: Vaibhav Ganeriwala
Date: 2025-04-19
Description: This script finds the cube of a given number.
"""

def cube_of_number_using_lambda(num):

    cube = lambda x: x ** 3
    return cube(num)

if __name__ == "__main__":
    try:
        number = float(input("Enter a number to find its cube: "))
        print(f"The cube of {number} is {round(cube_of_number_using_lambda(number), 2)}.")
    except ValueError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")