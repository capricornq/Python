# -*- coding: utf-8 -*-
import json
import pygal
from pygal.style import LightColorizedStyle, RotateStyle

from countries_codes import get_country_code
# 将数据加载到一个列表中
filename = 'population_data.json'

with open(filename) as f:
	pop_data = json.load(f)
	
# 创建一个包含人口数量的字典
cc_populations = {}

for pop_dict in pop_data:
	if pop_dict['Year'] == '2010': 
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		#print(country_name+": "+ str(population))
		code =get_country_code(country_name)
		if code:
			cc_populations[code] = population
			#print(code + ": " + str(population))
		else:
			print('ERROR - ' + country_name )
			
# 根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {},{},{}

for cc, pop in cc_populations.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop
	elif pop < 1000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop
		
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))

wm_style = RotateStyle('#336699', base_style = LightColorizedStyle) #十六进制的RGB颜色,前两个字符表示红色分量，接下来的两个表示绿色分量，最后两个表示蓝色分量,base_style修改主题
wm = pygal.maps.world.World( style = wm_style)


wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_populaton.svg')











