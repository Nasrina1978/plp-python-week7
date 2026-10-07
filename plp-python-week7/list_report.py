# list_report.py - Part C List Report
items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# 1. Numbered list
print("Shopping items:")
for index in range(len(items)):
    print(f"{index+1}. {items[index]}")

# 2. Count how many have more than 4 letters
count = 0
for item in items:
    if len(item) > 4:
        count += 1

print(f"\nNumber of items with more than 4 letters: {count}")

# 3. Find longest item name - no shortcuts, loop comparison
longest = items[0]
for item in items:
    if len(item) > len(longest):
        longest = item

print(f"Longest item name: {longest}")