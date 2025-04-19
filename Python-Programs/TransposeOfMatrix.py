"""
Author: Vaibhav Ganeriwala
Date: 2025-04-19
Description: This script takes a user-input matrix as input and computes its transpose.
"""

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def main():
    # Input matrix from user
    rows = int(input("Enter the number of rows in the matrix: "))
    cols = int(input("Enter the number of columns in the matrix: "))
    
    matrix = []
    print("Enter the elements of the matrix row-wise:")
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print(f"Error: Expected {cols} elements, but got {len(row)}.")
            return
        matrix.append(row)
    print("Original Matrix:")
    for row in matrix:
        print(row)
    transposed_matrix = transpose_matrix(matrix)
    print("Transposed Matrix:")
    for row in transposed_matrix:
        print(row)

if __name__ == "__main__":
    main()