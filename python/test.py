
f_num = input()
num_ar = []
for x in range(int(f_num)):
    temp = input()
    num_ar.append(temp)
for num in num_ar:
    t = 0
    for i in range(len(num)):
        t = t + int(num[i])
    if int(num) % t :
        print("NO")
    else:
        print("YES")
