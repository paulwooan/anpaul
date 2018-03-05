import time
import sys

i = (int(raw_input("Start countdown from? ")))+1

while i > 0:
    i-=1
    print i 
    time.sleep(1)

    if i == 0:
        print "BLAST OFF"