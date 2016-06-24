count=0
for pennies in range(0, 201):
    print pennies
    for twos in range(0, 101):
        for fives in range(0, 41):
            for tens in range(0, 21):
                for twenties in range(0, 11):
                    for fifties in range(0, 5):
                        for pounds in range(0, 3):
                            for twopounds in range(0, 2):
                                if (pennies + (twos*2) + (fives*5) + (tens*10) + (twenties*20) + (fifties*50) + (pounds*100) + (twopounds*200) == 200):
                                    count = count + 1
print "answer: %s" % (count)

