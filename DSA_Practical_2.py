# List of IDs
id_list = [478292, 473429, 430492, 491203, 430204, 410931]
print(id_list)
# Linear search
target_id = int(input("Sequential search\nEnter your ID: "))
for i in id_list:
    if target_id == i:
        print("IDs found at index:", id_list.index(i))
        break
else:
    print("Invalid ID")
print("\n Time Complexity = O(n).\n Space Complexity = O(1)")


# Binary search
id_list.sort()
print(id_list)

key = int(input("\nBinary Search\nEnter your ID: "))
l = 0
h = len(id_list) - 1

while l <= h:
    m = (l + h) // 2
    if id_list[m] == key:
        print("Your ID is verified, at index:", m)
        break
    elif id_list[m] < key:
        l = m + 1
    else:
        h = m - 1
else:
    print("ID not found")
print("\n Time Complexity = O(log(n)).\n Space Complexity = O(1)")