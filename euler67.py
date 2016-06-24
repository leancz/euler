
f=open("triangle.txt")
tree=[]

for i in f.readlines():
    print i
    tree.append(map(lambda a:int(a), i.split()))

f.close()
print tree

for i in range(1, len(tree)):
    for j in range(0, len(tree[i])):
        if j == 0:
            tree[i][j]=tree[i][j]+tree[i-1][0]
        else:
            if j == len(tree[i])-1:
                tree[i][j]=tree[i][j]+tree[i-1][j-1]
            else:
                if tree[i-1][j-1] > tree[i-1][j]:
                    tree[i][j]=tree[i][j]+tree[i-1][j-1]
                else:
                    tree[i][j]=tree[i][j]+tree[i-1][j]

print max(tree[i])

        
            

