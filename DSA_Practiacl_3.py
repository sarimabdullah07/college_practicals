'''
finding the top 5 salaries of employes and also sorting
all the salaries of employee by bubble and selection sorts
'''

def sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    print(a)
    l=[]
    for k in range(5):
        l.append(a[-1-k])
    print(l)

a=[32000,73000,92000,45000,21500,54000,64500,35750]
sort(a)