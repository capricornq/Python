# -*- coding: utf-8 -*-
#from pygal.i18n import COUNTRIES'''pygal.i18n在2.0版已经停止了，安装了以下的maps.world
from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code
	return None

'''print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))

for country_code in sorted(COUNTRIES.keys()):
	print(country_code, COUNTRIES[country_code])
'''
