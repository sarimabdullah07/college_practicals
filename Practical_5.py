
SIZE = 10
hash_table = [[] for i in range(SIZE)]

while True:
    print("\n--- HASH TABLE USING CHAINING ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Insert
    if choice == 1:
        key = int(input("Enter Key: "))
        value = input("Enter Value: ")

        index = key % SIZE
        found = False

        for i in range(len(hash_table[index])):
            if hash_table[index][i][0] == key:
                hash_table[index][i] = (key, value)
                found = True
                print("Key Updated Successfully!")
                break

        if found == False:
            hash_table[index].append((key, value))
            print("Key Inserted Successfully!")

    # Search
    elif choice == 2:
        key = int(input("Enter Key to Search: "))
        index = key % SIZE
        found = False

        for k, v in hash_table[index]:
            if k == key:
                print("Value Found:", v)
                found = True
                break

        if found == False:
            print("Key Not Found!")

    # Delete
    elif choice == 3:
        key = int(input("Enter Key to Delete: "))
        index = key % SIZE
        found = False

        for item in hash_table[index]:
            if item[0] == key:
                hash_table[index].remove(item)
                found = True
                print("Key Deleted Successfully!")
                break

        if found == False:
            print("Key Not Found!")

    # Display
    elif choice == 4:
        print("\nHash Table:")
        for i in range(SIZE):
            print(i, ":", hash_table[i])

    # Exit
    elif choice == 5:
        print("Program Exited!")
        break

    else:
        print("Invalid Choice!")
