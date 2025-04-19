"""
Author: Vaibhav Ganeriwala
Date: 2025-04-19
Description: This script takes a character input from the user and prints its ASCII value and vice-versa.
"""

def get_ascii_value(character):
    return ord(character)

def get_character(ascii_value):
    return chr(ascii_value)


def main():

    choice = input("Press 1 to get ASCII value of a character or 2 to get character from ASCII value: ")
    
    if choice == '1':
        character = input("Enter a character: ")
        
        # Check if the input is a single character
        if len(character) != 1:
            print("Please enter a single character.")
            return
        
        # Get ASCII value of the character
        ascii_value = get_ascii_value(character)
        print(f"The ASCII value of '{character}' is {ascii_value}.")
    
    elif choice == '2':
        # Get ASCII value input from user
        ascii_value_input = int(input("Enter an ASCII value: "))
        
        # Get character from ASCII value
        character_from_ascii = get_character(ascii_value_input)
        print(f"The character corresponding to ASCII value {ascii_value_input} is '{character_from_ascii}'.")
    
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()