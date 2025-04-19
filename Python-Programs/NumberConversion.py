"""
Author: Vaibhav Ganeriwala
Date: 2025-04-19
Description: This script takes user input and converts it to binary, octal, and hexadecimal formats and vice versa.
"""

def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def decimal_to_octal(n):
    return oct(n).replace("0o", "")

def decimal_to_hexadecimal(n):
    return hex(n).replace("0x", "").upper()

def binary_to_decimal(b):
    return int(b, 2)

def octal_to_decimal(o):
    return int(o, 8)

def hexadecimal_to_decimal(h):
    return int(h, 16)

def main():
    """Main function to handle user input and conversion."""
    print("Number Conversion Tool")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("4. Binary to Decimal")
    print("5. Octal to Decimal")
    print("6. Hexadecimal to Decimal")
    
    choice = input("Select an option (1-6): ")
    
    if choice in ['1', '2', '3']:
        num = int(input("Enter a decimal number: "))
        if num < 0:
            raise ValueError("Negative numbers are not supported.")
        if choice == '1':
            print(f"Binary: {decimal_to_binary(num)}")
        elif choice == '2':
            print(f"Octal: {decimal_to_octal(num)}")
        elif choice == '3':
            print(f"Hexadecimal: {decimal_to_hexadecimal(num)}")
    
    elif choice in ['4', '5', '6']:
        num = input("Enter the number: ")
        if choice == '4' and not all(bit in "01" for bit in num):
            raise ValueError("Invalid binary number.")
        elif choice == '5' and not all(bit in "01234567" for bit in num):
            raise ValueError("Invalid octal number.")
        elif choice == '6' and not all(bit in "0123456789ABCDEFabcdef" for bit in num):
            raise ValueError("Invalid hexadecimal number.")
        if choice == '4':
            print(f"Decimal: {binary_to_decimal(num)}")
        elif choice == '5':
            print(f"Decimal: {octal_to_decimal(num)}")
        elif choice == '6':
            print(f"Decimal: {hexadecimal_to_decimal(num)}")
    
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")