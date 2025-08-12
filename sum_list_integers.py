# Challenge 1: Create a list of integers from user input and compute the sum

# Get integers from user input
numbers = input("Enter integers separated by spaces: ").split()

# Convert to integers
numbers = [int(num) for num in numbers]

# Compute sum
total = sum(numbers)

# Display result
print("Sum of integers:", total)
