n = int(input("Number of elements : "))
arr = map(int, input("Values : ").split())
lis = list(arr)
for i in range(n):
        for j in range(i,n):
            if(lis[i]>lis[j]):
                lis[i],lis[j]=lis[j],lis[i]
for k in range(n-1,-1,-1):
    if(lis[k]!=lis[k-1]):
        break
print(lis[k-1])