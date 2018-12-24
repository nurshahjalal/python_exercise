import datetime
import pytz

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())


print(pytz.all_timezones)

for x in pytz.all_timezones:
    print(x)
country = "US/Eastern"

tz_to_display = pytz.timezone(country)
print(tz_to_display)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {} ".format(country, local_time))