#If the numbers 1 to 5 are written out in words: one, two, three, four, five,
#  then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used? 

unit = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]


def printThousands(n):
    if n < 1000: return ""
    return unit[(n/1000)-1] + "thousand"

def printHundreds(n):
    if n==1000: return ""
    if n < 100: return ""
    if n > 999:
        n = n - ((n / 1000) * 1000)
    return unit[(n/100)-1] + "hundred"

def printRest(n):
    output = ""
    if n > 100: output = "and"
    n = n - (( n / 100 ) * 100)
    if n == 0: return ""

    if n < 10:
        output=output + unit[n-1]
        return output
    if (n > 10) and (n < 20):
        output=output + teens[n-11]
        return output
    output=output+tens[(n/10)-1]
    units=n - ((n/10)*10)
    if units != 0:
        output=output+unit[units-1]
    
    
    return output
    
    
    
q=""
for i in range(1, 1001):
    q=q+ printThousands(i) + printHundreds(i) + printRest(i)

print len(q)









