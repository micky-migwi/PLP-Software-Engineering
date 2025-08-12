# Challenge 4: Two sets & common elements

# Create first set
set1 = set(map(int, input("Enter integers for Set 1 (space-separated): ").split()))

# Create second set
set2 = set(map(int, input("Enter integers for Set 2 (space-separated): ").split()))

# Find common elements
common_elements = set1.intersection(set2)

# Display result
print("Common elements in both sets:", common_elements)
# Challenge 4: Two sets & common elements
# Create first set