n = int(input().strip())
if(n%2!=0):
  print("Weird")
elif(n%2==0):
  if n in range(2,6):
    print("Not Weird")
  elif 6<=n<=20:
    print("Weird")
  elif n>20:
    print("Not Weird")