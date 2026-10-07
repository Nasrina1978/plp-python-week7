# PLP Python Week 7 - Shopping List Manager

## Files Description
- **list_warmup.py**: Warmup demonstrating creating a list, accessing first/last by index, using .append(), .remove() and len().
- **shopping_list.py**: Interactive shopping list manager with add/remove/show/done menu that never crashes.
- **list_report.py**: Generates a numbered report, counts items longer than 4 letters, and finds the longest name using loops.

## Why check `in` before `.remove()`?
It is safer to check `if item in list` before calling `.remove()` because `.remove()` will raise a ValueError and crash the program if the item does not exist. Checking first lets us show a friendly message like "That item is not on your list" instead of crashing.
