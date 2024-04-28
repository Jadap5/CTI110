# Name: Jada Parker

# Date: April 28, 2024

# Assignment Name: P5HW_ParkerJada.py

# This program implements a math quiz game where users can practice addition and subtraction by solving randomly generated problems. It provides a menu-driven interface for user interaction, displays random numbers for addition and subtraction, and provides feedback on the correctness of the user's answers.

import random

def add_random_numbers():
    # Generate two random numbers
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    
    # Calculate the correct sum
    correct_sum = num1 + num2
    
    # Initialize the number of guesses
    number_of_guesses = 0
    
    # Display the numbers to the user
    print(f"{num1}\n+ {num2}")
    
    # Loop until the user guesses the correct sum
    while True:
        # Increment the number of guesses
        number_of_guesses += 1

        # Prompt the user to enter their answer
        user_answer = input("Enter answer: ")

        # Check if the user's input is numeric
        if not user_answer.isdigit():
            print("Please enter a valid number.")
            continue

        user_answer = int(user_answer)

        # Check if the user's answer is correct
        if user_answer == correct_sum:
            print(f"Congratulations!!!! Your answer is correct. Number of guesses: {number_of_guesses}")
            break  # Exit the loop, as the correct answer was guessed
        elif user_answer < correct_sum:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high.")
    
    # Return the number of guesses
    return number_of_guesses

def subtraction_quiz():
    # Generate two random numbers
    num1, num2 = generate_random_numbers()
    # Ensure num1 is greater than num2 for subtraction
    if num2 > num1:
        num1, num2 = num2, num1

    # Calculate the correct answer
    correct_answer = num1 - num2
    
    # Initialize guess count
    guess_count = 0
    while True:
        guess_count += 1
        # Prompt the user for their answer
        user_answer = input(f"What is the remainder when {num1} is subtracted by {num2}?\n")

        # Check if the user's input is numeric
        if not user_answer.isdigit():
            print("Please enter a valid number.")
            continue

        user_answer = int(user_answer)

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print(f"Congratulations!!!! Your answer is correct. Number of guesses: {guess_count}")
            break
        elif user_answer < correct_answer:
            print("Sorry, guess is too low. Try again:")
        else:
            print("Sorry, guess is too high. Try again:")

def generate_random_numbers():
    num1 = random.randint(1, 100)  # Generates a random integer between 1 and 100
    num2 = random.randint(1, 100)  # Generates another random integer between 1 and 100
    return num1, num2

def display_menu():
    print("Welcome to the Math Quiz Program!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit")

def math_quiz():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_random_numbers()
        elif choice == "2":
            subtraction_quiz()
        elif choice == "3":
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    math_quiz()
