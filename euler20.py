def factorial(n):
    product=1
    for i in range(1, n+1):
        product=product*i
    return product


sum=0
for i in str(factorial(100)):
    sum=sum+int(i)
    
print sum
    


