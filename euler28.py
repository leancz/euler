print "Spiral 1001 x 1001: %s" % (1001 * 1001)


sum = 1
for i in range(3, 1002, 2):
    sum=sum + (i ** 2)
    sum=sum + ((i - 1) ** 2 - (i - 2))
    sum=sum + ((i - 1) ** 2 + 1)
    sum=sum + (i ** 2) - (i - 1)

print "Sum: %s" % (sum)



