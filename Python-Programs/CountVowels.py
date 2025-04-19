"""
Author: Vaibhav Ganeriwala
Date: 2025-04-19
Description: This script inputs a string input and counts the number of each vowel (in dictionary format) in it.
"""

def count_vowels(input_string):
    vowels = "aeiou"
    vowel_count = {vowel: 0 for vowel in vowels}

    for char in input_string:
        if char in vowel_count:
            vowel_count[char] += 1

    return vowel_count

if __name__ == "__main__":
    try:
        input_string = input("Enter a string: ").lower()
        print("Vowel counts:", count_vowels(input_string))
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please enter a valid string.")