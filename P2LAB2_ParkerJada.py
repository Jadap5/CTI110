# Jada Parker
# February 26, 2024
# P2LAB2
# This project involves taking four floating-point numbers as input, calculating their product and average, and then outputting these values as rounded integers and floating-point numbers 

# Input the numbers
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

# Calculate product and average
product = num1 * num2 * num3 * num4
average = (num1 + num2 + num3 + num4) / 4

# Output rounded integers
print(f'{product:.0f}', end=' ')
print(f'{average:.0f}')

# Output floating-point numbers
print(f'{product:.3f}', end=' ')
print(f'{average:.3f}')
