a=[1,5,8,9,4,6,9,2]
b=[6,9,2,4,7,0,1,2]
c=[]
for i in range(len(a)):
    if a[i]<b[i]:
        c.append('меньше')
    elif a[i]>b[i]:
        c.append('больше')
    else:
        c.append('равны')
print(c)