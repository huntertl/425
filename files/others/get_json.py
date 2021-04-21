import json
import re
import requests

from pprint import pprint


def get_unit_script(r):
	for s in r.text.splitlines():
		if open_tag in s:
			return s


url="https://www.equityapartments.com/washington-dc/gallery-place-mt-vernon-triangle/425-mass-apartments"

r = requests.get(url)

open_tag = '    ea5.unitAvailability = '
close_tag = ';'
pattern = f"{open_tag}(.*?){close_tag}"
script = re.search(pattern, get_unit_script(r)).group(1)	#this is None if status_code is 404
# script = re.search(pattern, script).group(1)	#this is None if status_code is 404

units = json.loads(script)
# pprint(units)

with open('file.json','w') as f:
	pprint(units, stream=f)