"""
#import winsound
#import time
import os
import datetime

print(os.getcwd())
file_name = 'my_daily_data'
if not os.path.isfile(file_name):
    print("File doesn't exists")
f = open(file_name, "a+")
f.write(str(datetime.datetime.now())+'\n')
f.close()
work_time = 5
print(str(datetime.datetime.now()))
#time.sleep(work_time)
print(str(datetime.datetime.now()))
#winsound.PlaySound('siren.wav', winsound.SND_FILENAME)
print(str(datetime.datetime.now()))
print("hello")
"""

import time


def countdown(p, q):
    i = p
    j = q
    k = 0
    while True:
        if j == -1:
            j = 59
            i -= 1
        if j > 9:
            print(str(k)+str(i)+":"+str(j), end="\r")
        else:
            print(str(k)+str(i)+":"+str(k)+str(j), end="\r")
        time.sleep(1)
        j -= 1
        if i == 0 and j == -1:
            break
    if i == 0 and j == -1 :
        print("Goodbye!", end="\r")
        time.sleep(1)


countdown(1, 5) #countdown(min,sec)
