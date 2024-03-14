# Name: Jada Parker
# Date: 3/14/2024
# Assignment: P3LAB
# Description: This program checks if a given year is a leap year or not.

def is_leap_year(year):
    """
    Determines if a given year is a leap year or not.

    Args:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    year = int(input("Enter a year: "))

    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

if __name__ == "__main__":
    main()
