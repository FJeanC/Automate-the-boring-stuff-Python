import time

def calcProd():
    prod = 1
    for i in range(1, 100000):
        prod = prod * i
    return prod

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long' % (len(str(prod))))
print('Took {:.3f} seconds to calculate.'.format(endTime - startTime))

#  Different test
print(time.ctime())
thisMoment = time.time()
print(time.ctime(thisMoment))