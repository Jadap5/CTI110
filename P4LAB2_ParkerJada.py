def print_increment(start, end):
    if end < start:
        print("Second integer can't be less than the first.")
    else:
        while start <= end:
            print(start, end=" ")
            start += 5
        print()

# Taking input
start = int(input())
end = int(input())

# Calling the function
print_increment(start, end)
