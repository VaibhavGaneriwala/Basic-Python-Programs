"""
Author: Vaibhav Ganeriwala
Date: 2025-04-19
Description: This script checks if a given year is a leap year or not.
"""

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
if __name__ == "__main__":
    try:
        year = int(input("Enter a year to check if it's a leap year: "))
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")