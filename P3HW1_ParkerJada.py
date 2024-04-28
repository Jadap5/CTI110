#Jada Parker
#3/21/2024
#P3HW1
#This program takes a number grade , determines average and displays letter grade for average.

# Function to calculate the letter grade based on the average
def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# Main program
def main():
    # Enter grades for six modules
    mod_1 = float(input('Enter grade for Module 1: '))
    mod_2 = float(input('Enter grade for Module 2: '))
    mod_3 = float(input('Enter grade for Module 3: '))
    mod_4 = float(input('Enter grade for Module 4: '))
    mod_5 = float(input('Enter grade for Module 5: '))
    mod_6 = float(input('Enter grade for Module 6: '))

    # Add grades entered to a list
    grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

    # TO DO: determine lowest, highest, sum, and average for grades
    low = min(grades)
    high = max(grades)
    total = sum(grades)
    avg = total / len(grades)

    # Determine letter grade for average
    letter_grade = get_letter_grade(avg)

    # Display results
    print("\n-----------------Results-----------------")
    print(f"Lowest Grade: {low}")
    print(f"Highest Grade: {high}")
    print(f"Sum of Grades: {total}")
    print(f"Average: {avg:.2f}")
    print("-" * 45)
    print(f"Your grade is: {letter_grade}")

# Run the program
if __name__ == "__main__":
    main()
