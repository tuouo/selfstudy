#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# start_element, end_element, char_data
from xml.parsers.expat import ParserCreate
class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('start_element : %s, attr: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('end_element: %s' % name)
	
    def char_data(self, text):
        print('char_data: %s' % text)
		
xml = r'''<?xml version="1.0"?>					
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''		# keep r for safe, 
		# !!! #explanatory note still will be treat as a part of contents 
print(xml)
handle = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handle.start_element
parser.EndElementHandler = handle.end_element
parser.CharacterDataHandler = handle.char_data
parser.Parse(xml)
print("################################################")
	
data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''

from enum import Enum, unique
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

def tomorrow_name(today):
    return Weekday((Weekday[today].value + 1) % 7).name
	
class WeatherSaxHandler(object):
    def __init__(self):
        self.weathers = {}										# in class

    def start_element(self, name, attrs):
        if name == 'yweather:location':
            self.weathers['city'] = attrs['city']			
            self.weathers['country'] = attrs['country']			
        elif name == 'yweather:condition':
            self.today = attrs['date'].split(',')[0]
            self.tomorrow = tomorrow_name(self.today)
        elif name == 'yweather:forecast':
            if attrs['day'] == self.today or attrs['day'] == self.tomorrow:	
                dailyweather = {}
                dailyweather['text'] = attrs['text']
                dailyweather['low'] = int(attrs['low'])			# int()
                dailyweather['high'] = int(attrs['high'])
                if attrs['day'] == self.today:
                    self.weathers['today'] = dailyweather
                else:
                    self.weathers['tomorrow'] = dailyweather
		
def parse_weather(xml):
    handle = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handle.start_element
    parser.Parse(data)		
    return {
        'city': handle.weathers['city'],
        'country': handle.weathers['country'],
        'today': {
            'text': handle.weathers['today']['text'],
            'low': handle.weathers['today']['low'],
            'high': handle.weathers['today']['high']
        },
        'tomorrow': {
            'text': handle.weathers['tomorrow']['text'],
            'low': handle.weathers['tomorrow']['low'],
            'high': handle.weathers['tomorrow']['high']
        }
    }

weather = parse_weather(data)
print('Weather:', str(weather))
assert weather['city'] == 'Beijing', weather['city']
assert weather['country'] == 'China', weather['country']
assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
assert weather['today']['low'] == 20, weather['today']['low']
assert weather['today']['high'] == 33, weather['today']['high']
assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
assert weather['tomorrow']['low'] == 21, weather['tomorrow']['low']
assert weather['tomorrow']['high'] == 34, weather['tomorrow']['high']