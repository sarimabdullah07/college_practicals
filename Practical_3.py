
# Group B - Practical 1
# Undo and Redo using Stack

undo_stack = []
redo_stack = []

document = ""

while True:
    print("\n--- UNDO REDO SYSTEM ---")
    print("1. Make Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        undo_stack.append(document)

        change = input("Enter text to add: ")
        document += change

        redo_stack.clear()

        print("Change Added Successfully!")

    elif choice == 2:
        if undo_stack:
            redo_stack.append(document)
            document = undo_stack.pop()
            print("Undo Successful!")
        else:
            print("Nothing to Undo!")

    elif choice == 3:
        if redo_stack:
            undo_stack.append(document)
            document = redo_stack.pop()
            print("Redo Successful!")
        else:
            print("Nothing to Redo!")

    elif choice == 4:
        print("\nCurrent Document:")
        print(document)

    elif choice == 5:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")

# Stack follows LIFO principle.
