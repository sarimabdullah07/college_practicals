
SIZE = 10
hash_table = [None] * SIZE
DELETED = "DELETED"

while True:
    print("\n--- HASH TABLE USING LINEAR PROBING ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # INSERT
    if choice == 1:
        key = int(input("Enter Key: "))
        index = key % SIZE
        inserted = False

        for i in range(SIZE):
            pos = (index + i) % SIZE

            if hash_table[pos] == key:
                print("Key Already Exists!")
                inserted = True
                break

            if hash_table[pos] == None or hash_table[pos] == DELETED:
                hash_table[pos] = key
                print("Key Inserted Successfully!")
                inserted = True
                break

        if inserted == False:
            print("Hash Table is Full!")

    # SEARCH
    elif choice == 2:
        key = int(input("Enter Key to Search: "))
        index = key % SIZE
        found = False

        for i in range(SIZE):
            pos = (index + i) % SIZE

            if hash_table[pos] == None:
                break

            if hash_table[pos] == key:
                print("Key Found at Position:", pos)
                found = True
                break

        if found == False:
            print("Key Not Found!")

    # DELETE
    elif choice == 3:
        key = int(input("Enter Key to Delete: "))
        index = key % SIZE
        found = False

        for i in range(SIZE):
            pos = (index + i) % SIZE

            if hash_table[pos] == None:
                break

            if hash_table[pos] == key:
                hash_table[pos] = DELETED
                print("Key Deleted Successfully!")
                found = True
                break

        if found == False:
            print("Key Not Found!")

    # DISPLAY
    elif choice == 4:
        print("\nHash Table:")
        for i in range(SIZE):
            print(i, ":", hash_table[i])

    # EXIT
    elif choice == 5:
        print("Program Exited!")
        break

    else:
        print("Invalid Choice!")

