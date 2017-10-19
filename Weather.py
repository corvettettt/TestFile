# -*- coding: utf-8 -*-

import urllib2
import json
from city import city

cityname = raw_input('The weather of which city do you want to check?\n')
citycode = city.get(cityname)
if citycode:
  url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
  content  = urllib2.urlopen(url).read()
  data = json.loads(content)
  CityName= data['weatherinfo']['city']
  LowTemp= data['weatherinfo']['temp1']
  HighTemp= data['weatherinfo']['temp2']
  Weather = data['weatherinfo']['weather']
  Time = data['weatherinfo']['ptime']

print CityName+'\n'+Time+'\n'+LowTemp+' ~ '+HighTemp
