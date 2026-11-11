
# Group C - Practical 2
# Hash Table using Linear Probing

SIZE = 10

hash_table = [None] * SIZE
DELETED = "DELETED"

# Hash Function
def hash_function(key):
    return key % SIZE

# Insert Operation
def insert(key):
    index = hash_function(key)
    first_deleted = -1

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if hash_table[pos] == key:
            print("Key Already Exists!")
            return

        if hash_table[pos] == DELETED and first_deleted == -1:
            first_deleted = pos

        elif hash_table[pos] is None:
            if first_deleted != -1:
                pos = first_deleted

            hash_table[pos] = key
            print("Key Inserted Successfully!")
            return

    if first_deleted != -1:
        hash_table[first_deleted] = key
        print("Key Inserted Successfully!")
    else:
        print("Hash Table is Full!")

# Search Operation
def search(key):
    index = hash_function(key)

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if hash_table[pos] is None:
            break

        if hash_table[pos] == key:
            print("Key Found at Position:", pos)
            return

    print("Key Not Found!")

# Delete Operation
def delete(key):
    index = hash_function(key)

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if hash_table[pos] is None:
            break

        if hash_table[pos] == key:
            hash_table[pos] = DELETED
            print("Key Deleted Successfully!")
            return

    print("Key Not Found!")

# Display Operation
def display():
    print("\nHash Table:")
    for i in range(SIZE):
        print(i, ":", hash_table[i])

# Main Menu
while True:
    print("\n--- LINEAR PROBING ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter Key: "))
        insert(key)

    elif choice == 2:
        key = int(input("Enter Key to Search: "))
        search(key)

    elif choice == 3:
        key = int(input("Enter Key to Delete: "))
        delete(key)

    elif choice == 4:
        display()

    elif choice == 5:
        break

    else:
        print("Invalid Choice!")
