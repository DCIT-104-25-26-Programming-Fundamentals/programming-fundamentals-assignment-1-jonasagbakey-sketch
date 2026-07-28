# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================

# Function to read a matrix from the user
def read_matrix(rows, cols, name):
    print(f"\nEnter values for {name}:")
    matrix = []

    for i in range(rows):
        while True:
            row = list(map(int, input(f"Enter row {i + 1}: ").split()))
            if len(row) == cols:
                matrix.append(row)
                break
            else:
                print(f"Error: Please enter exactly {cols} numbers.")

    return matrix


# Function to display a matrix
def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:5}", end="")
        print()


# Part A: Transpose a matrix
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)

    return transpose


# Part B: Add two matrices
def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


# Part C: Multiply two matrices
def multiply_matrices(matrixA, matrixB):
    rowsA = len(matrixA)
    colsA = len(matrixA[0])
    colsB = len(matrixB[0])

    result = []

    for i in range(rowsA):
        row = []
        for j in range(colsB):
            total = 0
            for k in range(colsA):
                total += matrixA[i][k] * matrixB[k][j]
            row.append(total)
        result.append(row)

    return result


# =========================
# MAIN PROGRAM
# =========================

# ---------- Part A ----------
print("PART A - Matrix Transpose")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = read_matrix(rows, cols, "Matrix")

print("\nOriginal Matrix:")
display_matrix(matrix)

print("\nTransposed Matrix:")
display_matrix(transpose_matrix(matrix))


# ---------- Part B ----------
print("\nPART B - Matrix Addition")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix1 = read_matrix(rows, cols, "Matrix 1")
matrix2 = read_matrix(rows, cols, "Matrix 2")

result = add_matrices(matrix1, matrix2)

print("\nSum of Matrices:")
display_matrix(result)


# ---------- Part C ----------
print("\nPART C - Matrix Multiplication")

rowsA = int(input("Enter rows of Matrix A: "))
colsA = int(input("Enter columns of Matrix A: "))

matrixA = read_matrix(rowsA, colsA, "Matrix A")

rowsB = int(input("Enter rows of Matrix B: "))
colsB = int(input("Enter columns of Matrix B: "))

if colsA != rowsB:
    print("\nError: Matrix multiplication is not possible.")
    print("The number of columns in Matrix A must equal the number of rows in Matrix B.")
else:
    matrixB = read_matrix(rowsB, colsB, "Matrix B")

    product = multiply_matrices(matrixA, matrixB)

    print("\nProduct of Matrices:")
    display_matrix(product)
