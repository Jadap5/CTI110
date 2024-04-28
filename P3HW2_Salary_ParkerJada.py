# Jada Parker
# Date: 3/16/2024
# Assignment: P3HW2
# Description: This program calculates the gross pay for an employee based on the number of hours worked and pay rate.
"""
Pseudocode:
Start
    Define function calculate_gross_pay(hours_worked, pay_rate)
        Set regular_hours = 40
        Set overtime_rate = 1.5

        if hours_worked > regular_hours
            Calculate regular_pay as regular_hours * pay_rate
            Calculate overtime_hours as hours_worked - regular_hours
            Calculate overtime_pay as overtime_hours * pay_rate * overtime_rate
        else
            Set regular_pay = hours_worked * pay_rate
            Set overtime_hours = 0
            Set overtime_pay = 0

        Calculate gross_pay as regular_pay + overtime_pay
        Return regular_pay, overtime_pay, gross_pay, overtime_hours

    Ask user to enter employee's name
    Ask user to enter number of hours worked this week
    Ask user to enter employee's pay rate

    Call calculate_gross_pay function with hours_worked and pay_rate as arguments
    Store returned values (regular_pay, overtime_pay, gross_pay, overtime_hours)

    Display employee details
    Display regular_pay, overtime_pay, and gross_pay with appropriate formatting
End
"""
# Function to calculate the gross pay
def calculate_gross_pay(hours_worked, pay_rate):
    # Setting the hours before overtime kicks in
    regular_hours = 40
    overtime_rate = 1.5
    
    # Calculate regular and overtime pay
    if hours_worked > regular_hours:
        regular_pay = regular_hours * pay_rate
        overtime_hours = hours_worked - regular_hours
        overtime_pay = overtime_hours * pay_rate * overtime_rate
    else:
        regular_pay = hours_worked * pay_rate
        overtime_hours = 0
        overtime_pay = 0

    # Calculate total gross pay
    gross_pay = regular_pay + overtime_pay
    return regular_pay, overtime_pay, gross_pay, overtime_hours

# Get user input
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculate wages
regular_pay, overtime_pay, gross_pay, overtime_hours = calculate_gross_pay(hours_worked, pay_rate)

# Display the results
print("-------------------------------------")
print(f"Employee name: {employee_name}")
print("Hours Worked  Pay Rate  Overtime Hours  Overtime Pay  Regular Hour Pay  Gross Pay")
print("-------------------------------------------------------------------------------------")
print(f"{hours_worked:<13.2f} {pay_rate:<9.2f} {overtime_hours:<15.2f} ${overtime_pay:<13.2f} ${regular_pay:<15.2f} ${gross_pay:<10.2f}")
