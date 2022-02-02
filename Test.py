import datetime
import pytz

time = datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone("Europe/Berlin"))
dt_mtn = time.strftime("%B %A %d %H:%M")
print(dt_mtn)

#for tz in pytz.all_timezones:
 #   print(tz)