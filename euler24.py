#A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


def fac(n):
    sum=1
    for i in range(1,n+1):
        sum=sum*i
    return sum



def nth_seq(value, seq, test):
    print 'next_seq called with value ', value, 'seq', seq, 'test', test
    if len(seq) == 1:
        print seq[0]
        
    else:
        my_fac=fac(len(seq)-1)
        print 'factorial ',my_fac
        print 'testing seq + 1 == ', seq[test+1], ' value to test is ', seq[test+1] * my_fac
        if ((seq[test+1]*my_fac)+1 > value):
            # seq[test] is the value!
            print seq[test]
            value = value - seq[test]*my_fac
            del seq[test]
            test = 0
        else:
            # seq[0] is not the value
            test = test + 1
        nth_seq(value, seq, test)

def next_step(s):
    kpointer=len(s)-2
    while s[kpointer] <= s[kpointer-1]:
        kpointer = kpointer - 1
    
    for i in range(kpointer+1 ,len(s)):
        if s[i]>s[kpointer]: ipointer=i

    s[ipointer], s[kpointer] = s[kpointer], s[ipointer]

    s[ipointer+1:] = s[-1:ipointer+1:-1]

    return s

    
    
    




    


