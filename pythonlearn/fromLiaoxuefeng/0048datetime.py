#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
now = datetime.now()
print(now)
print(type(now))

oneday = datetime(1990, 6, 1)		
oneday = datetime(1990, 6, 1, 12, 1, 3, 4)
print(oneday)
print(oneday.timestamp())	
oneday = datetime(1970, 1, 1, 8)		
print(oneday)
print('\t', oneday.timestamp())			# 0, base on local time


seconds = 13544443.003
print(datetime.fromtimestamp(seconds))
print(datetime.utcfromtimestamp(seconds))
seconds = 0
print(datetime.fromtimestamp(seconds))	# local time, not utc


formate = '%Y-%m-%d %H:%M:%S'
sday = datetime.strptime('2015-06-1 12:02:39', formate)
print(sday)								# no message about timeZone

print(now.strftime(formate))
formate1 = '%a, %b, %d %H:%M'
print(now.strftime(formate1))


from datetime import timedelta
print(now)
print(now + timedelta(hours = 10))
print(now - timedelta(hours = 10, days = 1))
print()

from datetime import timezone
tz_utc8 = timezone(timedelta(hours = 8))
tz_utc7 = timezone(timedelta(hours = 7))
print(now.replace(tzinfo = tz_utc8))
print(now.replace(tzinfo = tz_utc7))

print(datetime.utcnow())
utc_dt = datetime.utcnow().replace(tzinfo = timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours = 8)))
print(bj_dt)
print(bj_dt.astimezone(timezone(timedelta(hours = 9.4))))

import re
def toTimeStamp(datetime_str, timezone_str):
    tz = re.match(r'^UTC([+|-])(\d+):([0|3]0)', timezone_str)
    if tz.group(1) == '+':
        tz = int(tz.group(2)) + int(tz.group(3)) / 60
    else:
        tz = - int(tz.group(2)) - int(tz.group(3)) / 60
    if abs(tz) >= 12:
        pass
    day = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    day += timedelta(hours = (8 - tz))
    return day.timestamp()

t1 = toTimeStamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
print(t1)
t2 = toTimeStamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
print(t2)
