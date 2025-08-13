num=[1,6,4,5,3]
target=11
res=0
for i in range(len(num)):
    for n in range(len(num)):
        if num[i]+num[n]==target:
            res=(num[i],num[n])
            print(i,n)
            break

print(res)


l=[1,2,3,5]
rotation = k%len(l)
