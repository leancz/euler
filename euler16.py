def emitLowestMagnitude(n):
    return n-((n/10)*10)


a = 2 ** 1000

sum = 0
while a > 0:
    sum=sum + emitLowestMagnitude(a)
    a = a / 10
    
print sum