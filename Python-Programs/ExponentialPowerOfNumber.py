"""
Author: Vaibhav Ganeriwala
Date: 2025-04-19
Description: This script takes user input of terms and calculates the exponential power of a number.
"""

def calculate_exponential_power(terms):
    return 2 ** terms

if __name__ == "__main__":
    terms = int(input("Enter the number of terms: "))
    print(f"2 raised to the power of {terms} is: {calculate_exponential_power(terms)}")