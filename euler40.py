#An irrational decimal fraction is created by concatenating the positive integers:
#
#0.123456789101112131415161718192021...
#
#It can be seen that the 12th digit of the fractional part is 1.
#
#If dn represents the nth digit of the fractional part, find the value of the following expression.
#
#d1  d10  d100  d1000  d10000  d100000  d1000000
#



a=""
n=1
while len(a) < 1000000:
    a = a + str(n)
    n = n + 1

sum=1
n=1
while n <= 1000000:
    sum=sum*int(a[n-1])
    n=n*10

print sum
