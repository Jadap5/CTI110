# Jada Parker
# February 26, 2024
# P2LAB1
# calculates the gas cost for driving certain distances based on user input of gas mileage and cost per gallon.

# Get input
mileage = float(input())
cost_per_gallon = float(input())

# Calculate gas cost for 20 miles, 75 miles, and 500 miles
miles = [20, 75, 500]
costs = [mile / mileage * cost_per_gallon for mile in miles]

# Output results
print(f'{costs[0]:.2f} {costs[1]:.2f} {costs[2]:.2f}')
