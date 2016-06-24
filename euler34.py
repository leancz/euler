#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.


import math

grandTotal=0

count=3
while count < 99999999:
    
    testVal=count
    sum=0
    while testVal > 0:
        sum = sum + math.factorial(testVal - (testVal / 10) * 10)
        testVal = testVal / 10
    if sum == count:
        print "found: %s" % (count)
        grandTotal=grandTotal + count
    count = count + 1

print grandTotal

