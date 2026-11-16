
event_queue = []

while True:
    print("\n--- EVENT PROCESSING SYSTEM ---")
    print("1. Add Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel Event")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Add Event
    if choice == 1:
        event = input("Enter Event Name: ")
        event_queue.append(event)
        print("Event Added Successfully!")

    # Process Event
    elif choice == 2:
        if len(event_queue) > 0:
            event = event_queue.pop(0)
            print("Processed Event:", event)
        else:
            print("Queue is Empty!")

    # Display Events
    elif choice == 3:
        if len(event_queue) > 0:
            print("\nPending Events:")
            for event in event_queue:
                print(event)
        else:
            print("No Pending Events!")

    # Cancel Event
    elif choice == 4:
        event = input("Enter Event Name to Cancel: ")

        if event in event_queue:
            event_queue.remove(event)
            print("Event Cancelled Successfully!")
        else:
            print("Event Not Found!")

    # Exit
    elif choice == 5:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")

