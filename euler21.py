#Let d(n) be defined as the sum of proper divisors of n 
#(numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair 
#and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 
#1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors 
#of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.


def d(n):
    """returns sum of proper divisors of n"""
    sum=0
    for i in range(1, n/2+2):
        if (n/i)*i == n: sum=sum+i
    return sum

#print d(220)
#print d(284)

found=[]
for i in range(1, 10000):
    d_i=d(i)
    d_d_i=d(d_i)
    if (d_d_i == i) and (i != d_i):
        if i not in found:
            found.append(i)
            found.append(d_i)
            print "found: %s and %s" % (i, d_i)
print sum(found)


