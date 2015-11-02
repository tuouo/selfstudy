#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum, unique
Month = Enum('Mon', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
					"Jul", 'Aug', 'Sep', "Oct", 'Nov', 'Dec'))
print(Month.Aug, Month['Aug'], Month['Aug'].value, Month(8))
for name, member in Month.__members__.items():
    print(name, '--', member, ',', member.value)
print(type(Enum), type(Month), isinstance(Month, Enum), issubclass(Month, Enum))
print(isinstance(Month.Aug, Month), isinstance(Month.Aug, Enum))
	
@unique				# check no value repeat
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
print(Weekday.Fri, Weekday['Fri'], Weekday(5), Weekday.Fri.value)
for name, member in Weekday.__members__.items():
    print(name, '--', member, ',', member.value)