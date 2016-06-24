def isPalindromic(testString):
    if testString == reverse(testString): return True
    return False

def reverse(sampleString):
    reversedString=""
    for i in range(len(sampleString)-1, -1, -1):
        reversedString = reversedString + sampleString[i]
    return reversedString


sum=0
for i in range(1, 1000000):
    if (i % 100000) == 0: print i
    if (isPalindromic(str(i))) and (isPalindromic(bin(i)[2:])): sum=sum+i
print "Sum %s" % (sum)


    


