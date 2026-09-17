'''
Q:03__finding the top 5 salaries of employes and also sorting
all the salaries of employee by bubble and selection sorts
'''
#Bubble sort
def sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    print("Salaries of employee\n",a)
    l=[]
    for k in range(5):
        l.append(a[-1-k])
    print("Top 5 Salaries\n",l)

a=[32000,73000,92000,45000,21500,54000,64500,35750]
sort(a)


# Selection sort
arr=[7500,9600,3502,3521,1475,8752,7685,9753,4852,1250]
for i in range(len(arr)-1):
    min=i
    for j in range(1+i,len(arr)):
        if arr[min]>arr[j]:
            min=j
    temp=arr[i]
    arr[i]=arr[min]
    arr[min]=temp
print("\n\nSalaries of employee:\n",arr,"\nTop 5 salaries:\n",arr[-5:])





