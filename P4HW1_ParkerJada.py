# Jada Parker
# April 12, 2024
# P4HW1

# A program to collect scores from the user, calculate the average after dropping the lowest score,
# and assign a letter grade based on the average.

# Prompt the user to enter the number of scores they want to input
num_scores = int(input("Enter the number of scores you would like to enter: "))

# Initialize an empty list to store the scores
scores = []

# Loop to collect the scores from the user
for i in range(num_scores):
    # Initialize a flag to control score input
    valid_score = False
    while not valid_score:
        score = int(input(f"Enter score {i + 1}: "))
        # Check if the score is within the valid range (0-100)
        if 0 <= score <= 100:
            scores.append(score)
            valid_score = True
        else:
            print("Invalid score. Please enter a score between 0 and 100.")

# Display the lowest score entered
lowest_score = min(scores)
print(f"Lowest score entered: {lowest_score}")

# Calculate the sum of scores after dropping the lowest score
sum_scores = sum(scores) - lowest_score

# Calculate the average of scores after dropping the lowest score
average_score = sum_scores / (num_scores - 1)
print(f"Average score after dropping lowest score: {average_score:.2f}")

# Determine the letter grade based on the average score
if average_score >= 90:
    print("Letter Grade: A")
elif 80 <= average_score < 90:
    print("Letter Grade: B")
elif 70 <= average_score < 80:
    print("Letter Grade: C")
elif 60 <= average_score < 70:
    print("Letter Grade: D")
else:
    print("Letter Grade: F")
