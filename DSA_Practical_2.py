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

#fibonacci search
set=[32,23,43,54,34,45,66,76,12,27]
#sorting
set.sort()
print(set)
#fabonacci series
a, b = 1, 1
c=[]
for _ in range(30):
    c.append(a)
    a, b = b, a + b
#c=fabonacci series
d=len(set)
#d=length of the array or list
for z in c:
    if d<=z:
        break
#fm = i
print(c)
print(z)