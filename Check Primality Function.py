num=int(input("Enter the number : "))
flag=True
for i in range(2,num):
    if(num%i==0):
        flag=False
if(flag==True):
    print(num,"is prime")
else:
    print(num,"is not prime")