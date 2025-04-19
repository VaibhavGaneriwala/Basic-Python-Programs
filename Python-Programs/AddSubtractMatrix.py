"""
Author: Vaibhav Ganeriwala
Date: 2025-04-19
Description: This script takes 2 matrices as input and performs addition and subtraction on them based on the user's choice.
"""

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def subtract_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

def main():
    try:
        print("Matrix Addition and Subtraction")
        
        rows1 = int(input("Enter number of rows for first matrix: "))
        cols1 = int(input("Enter number of columns for first matrix: "))
        matrix1 = []
        print("Enter elements of first matrix:")
        for i in range(rows1):
            row = list(map(int, input().split()))
            if len(row) != cols1:
                raise ValueError("Number of columns does not match the specified size.")
            matrix1.append(row)

        # Input for the second matrix
        rows2 = int(input("Enter number of rows for second matrix: "))
        cols2 = int(input("Enter number of columns for second matrix: "))
        matrix2 = []
        print("Enter elements of second matrix:")
        for i in range(rows2):
            row = list(map(int, input().split()))
            if len(row) != cols2:
                raise ValueError("Number of columns does not match the specified size.")
            matrix2.append(row)

        # Check if matrices can be added or subtracted
        if rows1 != rows2 or cols1 != cols2:
            print("Matrices must have the same dimensions to add or subtract.")
            return

        # Perform addition or subtraction
        choice = int(input("Enter 1 for Addition or 2 for Subtraction: "))
        
        if choice == 1:
            print("Result of Addition:")
            result_addition = add_matrices(matrix1, matrix2)
            print_matrix(result_addition)
        elif choice == 2:
            print("Result of Subtraction:")
            result_subtraction = subtract_matrices(matrix1, matrix2)
            print_matrix(result_subtraction)
        else:
            print("Invalid choice. Please enter 1 or 2.")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()