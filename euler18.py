tree=[[75], [95, 64],[17, 47, 82],[18, 35, 87, 10],[20, 04, 82, 47, 65],
[19, 01, 23, 75, 03, 34],[88, 02, 77, 73, 07, 63, 67],
[99, 65, 04, 28, 06, 16, 70, 92],[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23]]


for i in range(1, len(tree)):
    for j in range(0, len(tree[i])):
        if j == 0:
            tree[i][j]=tree[i][j]+tree[i-1][0]
        else:
            if j == len(tree[i])-1:
                tree[i][j]=tree[i][j]+tree[i-1][j-1]
            else:
                if tree[i-1][j-1] > tree[i-1][j]:
                    tree[i][j]=tree[i][j]+tree[i-1][j-1]
                else:
                    tree[i][j]=tree[i][j]+tree[i-1][j]

print max(tree[i])

        
            

#If this doesn't pique the interest of my fellow developers then I don't know
# what will: a problem that will take twenty billion years to solve (at an 
# extremely optimistic estimate), unless we find an efficient algorithm.
# The problem in question is Project Euler Problem 67. We're given a triangle 
#made up of one hundred rows of numbers, and asked to consider all routes from 
#the top to the bottom, made by moving from one row to the next via adjacent
# cells. Over all such routes, we have to find the maximum sum. Can't picture it? Let me help:

 

#For the route that I've drawn, the sum is 5 + 15 + 29 + 45 = [train your brain and work it out yourself!]. 

#If we only wanted to tackle the baby brother of this problem (Problem 18 - the
# same problem for a triangle with just 15 rows), we could get away with 
#checking each of the routes. But it's not feasible to do that here because 
#there are 299 possibilities: hence the need for an efficient algorithm. Any ideas?

#You could take a bath and wait for the Eureka moment. Or if you want to 
#avoid the ensuing streaking, read on.

#An algorithm
#Suppose that for each cell in a row we know the maximum sum over all routes
# ending at that cell. From that it's easy to work out the same for each 
#of the cells in the next row. Here's how you do it. If you've got a cell
# with value c, somewhere in the middle of the row, then you can only reach 
#it from either of the two cells adjacent to it in the row above.  


#We're assuming that we already know the maximum sum for routes ending at 
#these cells: suppose it is a and b respectively. So the biggest possible 
#sum we can get for routes ending at c is Max(c + a, c + b). For the 
#two cells at either end of the row the calculation is even simpler: 
#they can only be reached from the cell at the appropriate end of the row 
#above them, so we just sum the cell value with the known maximum sum to 
#the cell above. In this way, we can crunch through the rows, 'flattening' 
#the triangle until we reach the last row, at which point we will know 
#the maximum possible sum over all routes ending at each of the cells in that row.

#That's the middle of an algorithm. To solve the overall problem we just 
#need to add a beginning and an end. The middle part starts by assuming 
#that we already know the maximum sum for all routes ending at a particular 
#row. So to get the algorithm rolling we need a row for which we do have that 
#information, and the first row of the triangle is the obvious candidate: 
#all routes start there, so the maximum up to that point is just the value 
#of the cell in that row. How about the end of the algorithm? To solve the 
#problem, we need to know the maximum sum from top to bottom through the 
#triangle; we've calculated the maximum sum ending at each of the cells in 
#the last row, so we just need to take the maximum over all these cells.



