from matrix_tool import (
    input_matrix,
    add_matrices,
    subtract_matrices,
    multiply_matrices,
    transpose_matrix,
    determinant_matrix
)

print("=== Matrix Operations Tool ===")

print("\nChoose Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Transpose")
print("5. Determinant")

try:
    choice = int(input("\nEnter your choice (1-5): "))
except ValueError:
    print("Invalid input. Please enter a number from 1 to 5.")
    exit(1)

# Operations

if choice == 1:
    print("\nEnter First Matrix")
    matrix1 = input_matrix()

    print("\nEnter Second Matrix")
    matrix2 = input_matrix()

    result = add_matrices(matrix1, matrix2)
    print("\nAddition Result:")
    print(result)

elif choice == 2:
    print("\nEnter First Matrix")
    matrix1 = input_matrix()

    print("\nEnter Second Matrix")
    matrix2 = input_matrix()

    result = subtract_matrices(matrix1, matrix2)
    print("\nSubtraction Result:")
    print(result)

elif choice == 3:
    print("\nEnter First Matrix")
    matrix1 = input_matrix()

    print("\nEnter Second Matrix")
    matrix2 = input_matrix()

    result = multiply_matrices(matrix1, matrix2)
    print("\nMultiplication Result:")
    print(result)

elif choice == 4:
    print("\nEnter Matrix")
    matrix1 = input_matrix()

    result = transpose_matrix(matrix1)
    print("\nTranspose Result:")
    print(result)

elif choice == 5:
    print("\nEnter Matrix")
    matrix1 = input_matrix()

    result = determinant_matrix(matrix1)
    print("\nDeterminant:")
    print(result)

else:
    print("Invalid Choice")
    exit(1)