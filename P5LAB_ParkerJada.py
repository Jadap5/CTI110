def days_in_feb(user_year):
    if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
        return 29
    else:
        return 28

def main():
    user_year = int(input())
    feb_days = days_in_feb(user_year)
    print(f"{user_year} has {feb_days} days in February.")

if __name__ == "__main__":
    main()
