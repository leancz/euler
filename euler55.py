


def isLychrel(count, n):
    if count < 1: return False
    n = n + reverse(n)
    if not isPalin(n):
        return isLychrel(count - 1, n)
    return True

def reverse(n):
    s=str(n)
    t=""
    for i in range(len(s)-1, -1, -1):
        t=t+s[i]
    return int(t)

def isPalin(n):
    return n == reverse(n)
    


count = 0
for i in range(1, 10001):
    if not isLychrel(50, i):
        count=count + 1

print count





    