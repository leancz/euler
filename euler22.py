
f=open("names.txt")
names=[]

name_list=f.readline()
print name_list
f.close()

b=name_list.split(',')

b.sort()
a=[]
for i in b:
    a.append(i.strip('"'))


sum=0
for i in range(1, len(a)+1):
    thisword=0
    for j in a[i-1]:
        thisword=thisword+ord(j)-64
    sum=sum+thisword*i
    
print sum



