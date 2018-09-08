# 斑马题
str = input()
result=[]
temp=0
for i in range(len(str)-1):
    if str[i] != str[i+1]:
        temp=temp+1
    else:
        result.append(temp+1)
        temp=0
result.append(temp+1)
if str[0] != str[-1]:
    result[0] = result[0]+result[-1]
res=0
for r in result:
    if res<r:
        res=r

print(res)