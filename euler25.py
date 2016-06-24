def fibonacci():
    lowerTerm = 1
    higherTerm = 1
    yield 1
    yield 1
    while 1:
        newTerm = lowerTerm + higherTerm
        yield newTerm
        lowerTerm=higherTerm
        higherTerm=newTerm

count = 0
for i in fibonacci():
    count = count + 1
    if i > 10 ** 999:
        print count, i
        break


    


        