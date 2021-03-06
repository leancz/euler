#The sequence of triangle numbers is generated by adding the natural numbers.
#So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
#The first ten terms would be:
#
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
#Let us list the factors of the first seven triangle numbers:
#
# 1: 1
# 3: 1,3
# 6: 1,2,3,6
#10: 1,2,5,10
#15: 1,3,5,15
#21: 1,3,7,21
#28: 1,2,4,7,14,28
#We can see that 28 is the first triangle number to have over five divisors.
#
#What is the value of the first triangle number to have over five hundred divisors?
#



class linkedList():
    
    def __init__(self):
        self.head=None
        self.tail=None
        self.listStructure=[]
        self.currentNode=None # focus for iterating
        
    def resetPosition(self):
        self.currentNode=None

    def setPosition(self, value):
        self.currentNode=value
                
    def getNext(self):
        if self.currentNode is None:
            if self.head is None: return None
            self.currentNode=self.head
        else:
            self.currentNode=self.listStructure[self.currentNode][1]    
        if self.currentNode is None: return None # reached end of list        
        return self.listStructure[self.currentNode][2]
            
    
    def addNode(self, value):
        if self.tail is not None:
            self.listStructure.append((self.tail, None, value))
            self.listStructure[self.tail]=(self.listStructure[self.tail][0],
                len(self.listStructure)-1, self.listStructure[self.tail][2])
            self.tail=len(self.listStructure)-1
            
        else:
            self.listStructure.append((None, None, value))
            self.head=len(self.listStructure)-1
            self.tail=len(self.listStructure)-1
            
    def getPosition(self, value):
        index=self.head
        if self.head is not None:
            if self.listStructure[index][2] == value: return index
            if self.listStructure[index][1] is None: return None
            while self.listStructure[index][1] is not None:
                if self.listStructure[index][2] == value: return index
                index=self.listStructure[index][1]
            if self.listStructure[index][2] == value: return index
        return None
    
    def removeNode(self, value):
        indexToRemove=self.getPosition(value)
        if indexToRemove is None: print "invalid value error"

        if self.listStructure[indexToRemove][0] is not None: #if not head
            self.listStructure[self.listStructure[indexToRemove][0]] = (self.listStructure[self.listStructure[indexToRemove][0]][0], self.listStructure[indexToRemove][1], self.listStructure[self.listStructure[indexToRemove][0]][2])
                  # set prev to point to next
        else:
            self.head = self.listStructure[indexToRemove][1] # set head to point to next
        
        if self.listStructure[indexToRemove][1] is not None: # if not tail
            self.listStructure[self.listStructure[indexToRemove][1]] = (self.listStructure[indexToRemove][0], self.listStructure[self.listStructure[indexToRemove][1]][1], self.listStructure[self.listStructure[indexToRemove][1]][2])
        else:
            self.tail = self.listStructure[indexToRemove][0]
                  # set next to point to prev            

    def removeCurrentNode(self):
        if self.currentNode is None: return None
        indexToRemove=self.currentNode

        if self.listStructure[indexToRemove][0] is not None: #if not head
            self.listStructure[self.listStructure[indexToRemove][0]] = (self.listStructure[self.listStructure[indexToRemove][0]][0], self.listStructure[indexToRemove][1], self.listStructure[self.listStructure[indexToRemove][0]][2])
                  # set prev to point to next
        else:
            self.head = self.listStructure[indexToRemove][1] # set head to point to next
        
        if self.listStructure[indexToRemove][1] is not None: # if not tail
            self.listStructure[self.listStructure[indexToRemove][1]] = (self.listStructure[indexToRemove][0], self.listStructure[self.listStructure[indexToRemove][1]][1], self.listStructure[self.listStructure[indexToRemove][1]][2])
        else:
            self.tail = self.listStructure[indexToRemove][0]
                  # set next to point to prev            
        return 0


def primeNumbers(n=50000):
    """Returns prime numbers from 2"""
    #uses linked list instead of list
    numberList=linkedList()
    for i in range(2,n+1):
        numberList.addNode(i)

    
    prime = 2 #first prime_number
    
    while prime*prime < n:
        position=numberList.getPosition(prime)
        numberList.setPosition(position)
        i=numberList.getNext()
        while i is not None:
            if i % prime == 0:
                rc=numberList.removeCurrentNode()
                if rc is None: print "error removing node"
            i=numberList.getNext()
        position=numberList.getPosition(prime)
        numberList.setPosition(position)
        prime=numberList.getNext()
        
    numberList.resetPosition()
    
    i = numberList.getNext()
    while i is not None:
        yield i
        i = numberList.getNext()

#
#Is there an easier way other than trial and error to find the number 
#less than 100 that has the greatest number of factors?
#

#Date: 01/04/99 at 11:04:48
#From: Doctor Rob
#Subject: Re: How to Factor
#
#Thanks for writing to Ask Dr. Math!
#
#Yes, there is an easier way.
#
#If you factor a number into its prime power factors, then the total
#number of factors is found by adding one to all the exponents and
#multiplying those results together. Example: 108 = 2^2*3^3, so the 
#total number of factors is (2+1)*(3+1) = 3*4 = 12. Sure enough, the
#factors of 108 are 1, 2, 3, 4, 6, 9, 12, 18, 27, 36, 54, and 108.
#This happens because to be a factor, a number must have the same 
#primes, and raised to the same or lower powers. Each factor of 108 must 
#be a power of 2 times a power of 3, and the exponent of 2 can be 0, 1, 
#or 2, and the exponent of 3 can be 0, 1, 2, or 3. There are three 
#choices for the exponent of 2 and 4 choices for the exponent of 3, for 
#a total of 3*4 = 12 possible choices. Each gives a different factor, so 
#there are 12 factors.
#
#Now to create small numbers with many factors, you should use the
#smallest primes. The larger the exponents, the more factors you will
#have, but you have to keep the number less than 100, so the exponents
#cannot be too large.
#
#If there is only one prime, it should be 2. To stay less than 100,
#the exponent can be at most 6, since 2^7 = 128 > 100. 2^6 = 64 has
#6+1 = 7 factors.
#
def numberOfPrimeFactors(n):
    limit=100 # artificial limit
    for i in range(1, limit):
        if (2 ** i) > n: return i - 1
    return None

def primeExponentials(n):
    primeMaxExponential={}
    for i in primeNumbers():
        count=0
        while (i ** count) < n: count = count + 1
        primeMaxExponential[i] = count - 1
    return primeMaxExponential
    
def primeFactors(n):
    primeFactorDict={}
    for i in primeNumbers():
        primeFactorDict[i]=0
        while (n % i) == 0:
            primeFactorDict[i]=primeFactorDict[i]+1
            n = n / i
        if n == 1: return primeFactorDict



def numberOfFactors(n):
    product = 1
    for i in primeFactors(n).values():
        product = product * (i + 1)
    return product
    



#print numberOfPrimeFactors(200)
#print numberOfPrimeFactors(2000)

    
#If there are two primes, they should be 2 and 3. To stay less than 100, 
#the exponent of 3 can be at most 4, since 3^5 = 243 > 100. Consider 
#numbers of the form a power of 2 times 3, 3^2, 3^3, or 3^4. Pick the 
#power of 2 as large as possible while staying under 100. Compute the 
#number of factors, and keep the champion(s).
#
#If there are three primes, they should be 2, 3, and 5. To stay less
#than 100, the exponent of 5 can be at most 2, since 5^3 = 125 > 100.
#Consider numbers of the form a power of 2 times a power of 3 times 5 or 
#5^2. Pick a power of 3 which keeps you under 100, then pick the power 
#of 2 as large as possible while staying under 100. Compute the number 
#of factors, and keep the champion(s).
#
#There cannot be four or more primes, because 2*3*5*7 = 210 > 100.
#
#You get the following table, in which you can complete the last
#column:
#
#Exponent of 2   Exponent of 3   Exponent of 5    N   Number of Factors
#      6               0               0         64           7
#      5               1               0         96
#      3               2               0         72
#      0               3               0         81           4
#      4               0               1         80
#      2               1               1         60
#      1               2               1         90
#      1               0               2         50           6
#      0               1               2         75           6
#
#This systematic procedure is better than trial and error.
#
#

       
def triangleNumbers():
        currentNumber=1
        while 1:
            sum = 0
            for i in range(1, currentNumber + 1):
                sum=sum + i
            currentNumber = currentNumber + 1
            yield sum


def factors(n):
    factorList=[]
    for i in range(1, n + 1):
        if n % i == 0:
            factorList.append(i)
    return factorList

def factor_count(n):
    numFactors=0
    for i in range(1, n + 1):
        if n % i == 0:
            numFactors=numFactors + 1
    return numFactors



for i in triangleNumbers():
    factors=numberOfFactors(i)
    if (factors % 100) == 0: print "reached %s factors with n=%s" % (factors, i)
    if factors > 500:
        print i
        break



        
