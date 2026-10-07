# shopping_list.py - Part B Shopping List Manager
shopping_list = []

while True:
    action = input("\nWhat would you like to do? (add / remove / show / done): ").strip().lower()

    if action == "add":
        item = input("Enter item to add: ").strip()
        if item:
            shopping_list.append(item)
            print(f"'{item}' added to your list.")

    elif action == "remove":
        item = input("Enter item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed from your list.")
        else:
            print("That item is not on your list.")

    elif action == "show":
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            print("\nYour shopping list:")
            for i in shopping_list:
                print(f"- {i}")

    elif action == "done":
        print("Goodbye! Here is your final list:")
        for i in shopping_list:
            print(f"- {i}")
        break

    else:
        print("Invalid command. Use: add / remove / show / done")python shopping_list.py