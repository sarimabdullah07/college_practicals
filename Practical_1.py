
# Group A - Practical 1
# Library Book Borrowing Records

books = ["Python", "Java", "C++", "Data Structures", "DBMS"]
borrow_count = [10, 5, 0, 8, 5]

# Average borrowings
total = sum(borrow_count)
average = total / len(borrow_count)
print("\nAverage Borrowings:", average)

# Highest and lowest borrowings
highest = max(borrow_count)
lowest = min(borrow_count)

for i in range(len(books)):
    if borrow_count[i] == highest:
        print(books[i], ":", highest)
    if borrow_count[i] == lowest:
        print(books[i], ":", lowest)

# Count zero borrowings
zero_count = borrow_count.count(0)
print("\nZero Borrowing Members:", zero_count)

# Find mode
frequency = {}

for count in borrow_count:
    frequency[count] = frequency.get(count, 0) + 1

max_frequency = max(frequency.values())

print("\nMost Frequent Borrowing Count (Mode):")
for count, freq in frequency.items():
    if freq == max_frequency:
        print(count, "books borrowed")

# Complexity:
# Time Complexity: O(n)
# Space Complexity: O(n)
