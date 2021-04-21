import json
import os
import re

from pprint import pprint

IN_FILE = "file.html"
OUT_FILE = "file.json"

def get_line_from_file(file):
	global open_tag
	with open(IN_FILE) as f:
	 lines = f.readlines()
	for l in lines:
		if open_tag in l:
			return l


open_tag = '    ea5.unitAvailability = '
close_tag = ';'
pattern = f"{open_tag}(.*?){close_tag}"
blob = re.search(pattern, get_line_from_file(IN_FILE)).group(1)	

units = json.loads(blob)

with open(OUT_FILE,'w') as f:
	pprint(units, stream=f)


os.remove(IN_FILE)


# # w/ requests:
# 
# import requests
# 
# url="https://www.equityapartments.com/washington-dc/gallery-place-mt-vernon-triangle/425-mass-apartments"
# r = requests.get(url)


# # todo: implement
#
# import pandas as pd
#
# df = pd.concat([pd.DataFrame(x['AvailableUnits']) for x in units['BedroomTypes']])
# df.sort_values(by=['BuildingId', 'UnitId']).to_csv('table.csv')


