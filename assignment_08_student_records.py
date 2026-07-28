# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================

# Function to add a student
def add_student(students):
    name = input("Student name: ")
    student_id = input("Student ID: ")

    number_of_scores = int(input("How many scores? "))

    scores = []

    for i in range(number_of_scores):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }

    students.append(student)

    print(f'Student "{name}" added successfully.')


# Function to display all students
def display_students(students):
    if len(students) == 0:
        print("No students have been added yet.")
        return

    print("\n--------------------------------------------------")
    print("Name\t\tID\t\tScores\t\tAverage")
    print("--------------------------------------------------")

    for student in students:
        total = 0

        for score in student["scores"]:
            total += score

        average = total / len(student["scores"])

        scores = ", ".join(map(str, student["scores"]))

        print(
            f"{student['name']}\t{student['id']}\t{scores}\t{average:.2f}"
        )

    print("--------------------------------------------------")


# Function to calculate average score for a specific student
def calculate_average(students):
    student_id = input("Enter student ID: ")

    for student in students:

        if student["id"] == student_id:

            total = 0

            for score in student["scores"]:
                total += score

            average = total / len(student["scores"])

            print(
                f"{student['name']}'s average score: {average:.2f}"
            )

            return

    print("Error: Student ID not found.")


# Function to display menu
def display_menu():
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


# Main program
def main():

    students = []

    while True:

        display_menu()

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            calculate_average(students)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Error: Invalid choice. Please select between 1 and 4.")


# Run the program
main()
