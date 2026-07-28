# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================

# Part A: Generate a single multiplication table
def multiplication_table(number):
    print(f"\nMultiplication Table for {number}:")

    for i in range(1, 13):
        print(f"{number}  x  {i}  =  {number * i}")


# Part B: Generate multiplication tables from 1 to N
def multiple_tables(n):
    for number in range(1, n + 1):
        print(f"\nMultiplication Table for {number}:")

        for i in range(1, 13):
            print(f"{number}  x  {i}  =  {number * i}")

        print("---------------------------")


# =========================
# Main Program
# =========================

# Part A
num = int(input("Enter a number for multiplication table: "))

if num <= 0:
    print("Error: Number must be a positive integer.")
else:
    multiplication_table(num)


# Part B
n = int(input("\nEnter N to generate tables from 1 to N: "))

if n <= 0:
    print("Error: Number must be a positive integer.")
else:
    multiple_tables(n)
