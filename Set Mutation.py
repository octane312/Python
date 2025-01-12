m=int(input("Enter the number of elements in set A : "))
setA = set(map(int,input().split()))
N=int(input("Number of operations : "))
for _ in range(N):
    operation,n = input().split()
    setB = set(map(int,input().split()))
    if(operation == 'intersection_update'):
        setA.intersection_update(setB)
    elif(operation == 'update'):
        setA.update(setB)
    elif(operation == 'symmetric_difference_update'):
        setA.symmetric_difference_update(setB)
    elif(operation=='difference_update'):
        setA.difference_update(setB)

print(sum(setA))
    