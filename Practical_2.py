
# Group A - Practical 2
# Linear Search and Binary Search

accounts = [105, 120, 115, 130, 110, 140, 125]

print("Customer Account IDs:", accounts)

key = int(input("Enter Account ID to search: "))

# Linear Search
found = False

for i in range(len(accounts)):
    if accounts[i] == key:
        print("\nLinear Search: Account Found")
        print("Position:", i + 1)
        found = True
        break

if not found:
    print("\nLinear Search: Account Not Found")

# Binary Search
sorted_accounts = sorted(accounts)

print("\nSorted Account IDs:", sorted_accounts)

low = 0
high = len(sorted_accounts) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if sorted_accounts[mid] == key:
        print("Binary Search: Account Found")
        print("Position:", mid + 1)
        found = True
        break

    elif key < sorted_accounts[mid]:
        high = mid - 1

    else:
        low = mid + 1

if not found:
    print("Binary Search: Account Not Found")

# Linear Search: O(n)
# Binary Search: O(log n)
