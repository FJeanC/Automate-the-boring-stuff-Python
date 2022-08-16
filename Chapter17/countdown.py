#! python3
# countdown.py - A simple countdown script- plays a sound when countdown reaches zero

import time, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft -= 1
subprocess.Popen(['start', 'alarm.wav'], shell=True)