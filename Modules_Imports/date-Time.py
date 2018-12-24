

# https://docs.python.org/3/library/time.html

import time
from time import perf_counter as my_timer
from time import gmtime, strftime
import random


print(time.clock())
print(time.localtime())
print(time.time())
print(time.localtime().tm_hour)
print(time.gmtime())

print(time.timezone)

print(time.strftime(" %I", time.localtime()))

print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
print(strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime()))


print("==========")

t = time.strptime("23:34", "%H:%M")
time_value_12hour = time.strftime("%I:%M %p", t)
print(time_value_12hour)

print ("==========")
input("Press Enter to start")
wait_time = random.randint(1,6)
time.sleep(wait_time)
start_time = my_timer()

input("Please enter to stop")
end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Reaction Time was {} Seconds ".format(end_time - start_time))

