"""
Author: Vaibhav Ganeriwala
Date: 2025-04-19
Description: This script finds the HCF (Highest Common Factor) of two numbers using the Euclidean algorithm.
"""

def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    print(f"The HCF of {num1} and {num2} is: {hcf(num1, num2)}")