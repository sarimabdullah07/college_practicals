
# Group B - Practical 2
# Event Processing using Queue

from collections import deque

event_queue = deque()

while True:
    print("\n--- EVENT PROCESSING SYSTEM ---")
    print("1. Add Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel Event")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        event = input("Enter Event Name: ")
        event_queue.append(event)
        print("Event Added Successfully!")

    elif choice == 2:
        if event_queue:
            event = event_queue.popleft()
            print("Processed Event:", event)
        else:
            print("Queue is Empty!")

    elif choice == 3:
        if event_queue:
            print("\nPending Events:")
            for event in event_queue:
                print(event)
        else:
            print("No Pending Events!")

    elif choice == 4:
        event = input("Enter Event Name to Cancel: ")

        if event in event_queue:
            event_queue.remove(event)
            print("Event Cancelled Successfully!")
        else:
            print("Event Not Found!")

    elif choice == 5:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")

# Queue follows FIFO principle.
