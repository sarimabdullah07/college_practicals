borrow_books = [2,4,2,6,0,1,5,0,0,8,1,7,3,1,0]
count=0
total=0
zero=0
h=borrow_books[0]
l=borrow_books[0]
max_freq=0
mode=borrow_books[0]
#finding average
for i in borrow_books:
    total+=i
    count+=1
    #finding highest and lowest
    if i>h:
        h=i
    if i<l:
        l=i
    #finding 0 no. of borrowed
    if i==0:
        zero+=1
    #finding highest frequency
    freq=0
    for j in borrow_books:
        if j==0:
            continue
        if i==j:
            freq+=1
    if freq>max_freq:
        max_freq=freq
        mode=i
print(f"Average={round(total/count,2)}")
print(f"highest no. of book borrowed: {h}\nlowest no. of book borrowed: {l}")
print(f"Number of zero books borrowed: {zero}")
print(f"{mode} comes {max_freq} times")

print("Time Complexitiy if the given program is O(n²)\nAnd Space Complexitiy if the given program is O(1)")