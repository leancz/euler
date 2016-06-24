
XMAX = 20
YMAX = 20
count = 1

def getNext(x, y, count):
    
    if (x == XMAX) and (y == YMAX): # at the end
        return count
    else:
        if y == YMAX: # no branch
            count = getNext(x+1, y, count)
        else:
            if x == XMAX: # no branch
                count = getNext(x, y+1, count)
            # branch
            else:
                count = count + 1
                if (count % 100000000) == 0: print "Found %s routes" % (count)
                count = getNext(x+1, y, count)
                count = getNext(x, y+1, count)

        
    return count

x=0
y=0

#print getNext(x, y, count)

def generateNextRow(currentRow):
    nextRow=[]
    nextRow.append(1)
    for i in range(0,len(currentRow)-1):
        nextRow.append(currentRow[i] + currentRow[i+1])
    nextRow.append(1)
    return tuple(nextRow)
        
    
def pascalsTriangle(size):
    triangle=[(1,), (1,1)]
    if size < 3: return triangle[:size]
    while size > len(triangle):
        triangle.append(generateNextRow(triangle[-1]))
            
    return triangle


a=pascalsTriangle(42)
print a[40][len(a[40]) / 2]




    