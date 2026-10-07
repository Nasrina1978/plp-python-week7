# list_warmup.py - Part A List Warmup
fruits = ["mango", "banana", "apple", "orange"]

# Print first and last using indexes
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# Append a fifth fruit
fruits.append("pineapple")
print(f"After appending: {fruits}")

# Remove one fruit
fruits.remove("banana")
print(f"After removing banana: {fruits}")

# How many remain
print(f"Total fruits remaining: {len(fruits)}")