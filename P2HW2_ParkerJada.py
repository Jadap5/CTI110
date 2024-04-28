# Jada Parker
# 3/2/2024
# P2HW2
# This program prompts the user to enter grades for six modules, stores them in a list, and then displays the lowest grade, highest grade, sum
of rades, and the average of the grades.
# Initialize an empty list named "grades"
grades = []
# Prompt the user to enter the grade for Module 1 and add it to the list
module1_grade = float(input("Enter grade for Module 1: "))
grades.append(module1_grade)
# Prompt the user to enter the grade for Module 2 and add it to the list
module2_grade = float(input("Enter grade for Module 2: "))
grades.append(module2_grade)
# Prompt the user to enter the grade for Module 3 and add it to the list
module3_grade = float(input("Enter grade for Module 3: "))
grades.append(module3_grade)
# Prompt the user to enter the grade for Module 4 and add it to the list
module4_grade = float(input("Enter grade for Module 4: "))
grades.append(module4_grade)
# Prompt the user to enter the grade for Module 5 and add it to the list
module5_grade = float(input("Enter grade for Module 5: "))
grades.append(module5_grade)
# Prompt the user to enter the grade for Module 6 and add it to the list
module6_grade = float(input("Enter grade for Module 6: "))
grades.append(module6_grade)
# Display the lowest grade in the list
print("Lowest Grade:", min(grades))
# Display the highest grade in the list
print("Highest Grade:", max(grades))
# Calculate and display the sum of all grades in the list
print("Sum of Grades:", sum(grades))
# Calculate and display the average of all grades in the list with two decimal positions
average_grade = sum(grades) / len(grades)
print("Average Grade: {:.2f}".format(average_grade))
