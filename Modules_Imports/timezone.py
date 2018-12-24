import time
import pytz

print(time.tzname)
print("Epoch in this system starts at " + time.strftime("%c", time.gmtime()))

print("The Current Timezone is {0} with an offset of {1} ".format(time.tzname[0], time.timezone))


if time.daylight != 0:
    print("\tDaylight saving time is in effect for this location")
    print("\tThe DST timezone is " + time.tzname[1])

print("The local time is " + time.strftime("%Y-%m-%d %I:%M:%S ", time.localtime()))

