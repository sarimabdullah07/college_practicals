
# Group C - Practical 1
# Hash Table using Chaining

SIZE = 10

hash_table = [[] for i in range(SIZE)]

# Hash Function
def hash_function(key):
    return key % SIZE

# Insert Operation
def insert(key, value):
    index = hash_function(key)

    for i in range(len(hash_table[index])):
        if hash_table[index][i][0] == key:
            hash_table[index][i] = (key, value)
            print("Key Updated Successfully!")
            return

    hash_table[index].append((key, value))
    print("Key Inserted Successfully!")

# Search Operation
def search(key):
    index = hash_function(key)

    for k, v in hash_table[index]:
        if k == key:
            print("Value Found:", v)
            return

    print("Key Not Found!")

# Delete Operation
def delete(key):
    index = hash_function(key)

    for item in hash_table[index]:
        if item[0] == key:
            hash_table[index].remove(item)
            print("Key Deleted Successfully!")
            return

    print("Key Not Found!")

# Display Hash Table
def display():
    print("\nHash Table:")
    for i in range(SIZE):
        print(i, ":", hash_table[i])

# Main Menu
while True:
    print("\n--- HASH TABLE USING CHAINING ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter Key: "))
        value = input("Enter Value: ")
        insert(key, value)

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
