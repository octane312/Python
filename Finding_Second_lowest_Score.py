record=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    record.append([name,score])
grades=sorted(set([score for name,score in record]))
req_grade = grades[1]

req_name=[name for name,score in record if score==req_grade]

req_name.sort()

for i in req_name:
    print(i)
    