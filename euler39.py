#If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.
#
#{20,48,52}, {24,45,51}, {30,40,50}
#
#For which value of p  1000, is the number of solutions maximised?




# Length of hypoteneuse varies from max(x|y) to sqrt(2) * x (or y)
# Length of a cathetus varies from 0 to 0.5 * perimeter

import math

def triangleSidesOfPerimeter(perimeter):
    sides={}
    for c1 in range(1, perimeter / 2):
        #print "p = %s" % (perimeter)
        #print "c1 = %s" % (c1)
        for c2 in range(1, perimeter / 2):
            #print "c2 = %s" % (c2)
            hyp=math.sqrt((c1 ** 2) + (c2 ** 2))
            if hyp == perimeter - c1 - c2:
                #print "*** Found hyp == %s c1 == %s, c2 == %s" % (hyp, c1, c2)
                sides[hyp]=(c1,c2)
    return sides
        



maxSolutions=0
perimWithMax=0
for p in range(1,1001):
    print p
    solutions=len(triangleSidesOfPerimeter(p))
    if solutions > maxSolutions:
        maxSolutions = solutions
        perimWithMax=p

print "Perimeter %s has %s solutions" % (perimWithMax, maxSolutions)






    

