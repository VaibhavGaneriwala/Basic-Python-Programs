"""
Author: Vaibhav Ganeriwala
Date: 2025-04-19
Description: This script takes user input and reverses the string.
"""

def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string to reverse: ")
    print(f"Reversed string: {reverse_string(user_input)}")