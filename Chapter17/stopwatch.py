#! python3
# stopwatch.py - A simple stopwatch program - track the amount of time
# elapsed between presses of the enter key

import time

print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch.\
    press Ctrl-C to quit.')

input()
print('Started.')

startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum+=1
        lastTime = time.time()
except:
    # user pressed ctrl-c
    print('\nDone')

