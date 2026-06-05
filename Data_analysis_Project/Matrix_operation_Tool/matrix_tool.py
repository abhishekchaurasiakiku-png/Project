import numpy as np

def input_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []

    print("Enter matrix elements row by row:")

    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    return np.array(matrix)

def add_matrices(matrix1, matrix2):
    return matrix1 + matrix2

def subtract_matrices(matrix1, matrix2):
    return matrix1 - matrix2

def multiply_matrices(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

def transpose_matrix(matrix):
    return np.transpose(matrix)

def determinant_matrix(matrix):
    return np.linalg.det(matrix)