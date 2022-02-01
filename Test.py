import datetime
import pytz

dt_mtn = datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone("Europe/Berlin")).strftime("%B %d, %Y")
print(dt_mtn)

#for tz in pytz.all_timezones:
 #   print(tz)