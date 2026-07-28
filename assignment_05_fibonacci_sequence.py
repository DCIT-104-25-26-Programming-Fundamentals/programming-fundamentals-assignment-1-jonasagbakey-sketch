# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================

# Part A: Print the first N Fibonacci terms
def print_fibonacci(n):
    if n <= 0:
        print("Error: Number of terms must be a positive integer.")
        return

    first = 0
    second = 1

    print("Fibonacci sequence:", end=" ")

    for i in range(n):
        print(first, end=" ")
        next_num = first + second
        first = second
        second = next_num

    print()   # Move to the next line


# Part B: Check whether a number is a Fibonacci number
def check_fibonacci(number):
    if number < 0:
        print(f"{number} is NOT a Fibonacci number.")
        return

    first = 0
    second = 1

    while first < number:
        next_num = first + second
        first = second
        second = next_num

    if first == number:
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")


# =========================
# Main Program
# =========================

# Part A
n = int(input("How many terms? "))
print_fibonacci(n)

# Part B
num = int(input("Enter a number to check: "))
check_fibonacci(num)
