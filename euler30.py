

count = 2
grandTotal=0

while count < 10000000:
    testVal=count
    sum=0
    while testVal > 9:
        sum = sum + ((testVal - (testVal / 10) * 10) ** 5)
        testVal = testVal / 10
    sum = sum + testVal ** 5
    if sum == count: grandTotal=grandTotal + count
    count = count + 1

print grandTotal








