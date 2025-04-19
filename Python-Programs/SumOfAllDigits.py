"""
Author: Vaibhav Ganeriwala
Date: 2025-04-19
Description: This script takes user input and find the sum of all digits in the input.
"""

def sum_of_digits(number):
    num_str = str(number)
    total_sum = 0

    for digit in num_str:
        total_sum += int(digit)
    
    return total_sum

if __name__ == "__main__":
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        print(f"The sum of all digits in {user_input} is: {sum_of_digits(user_input)}")
    else:
        print("Please enter a valid number.")
