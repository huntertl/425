import json
import re
import urllib.request

IN_FILE = "file.html"
OUT_FILE = "_file.json"

URL = "https://www.equityapartments.com/washington-dc/gallery-place-mt-vernon-triangle/425-mass-apartments"

open_tag = '    ea5.unitAvailability = '
close_tag = ';'
pattern = f"{open_tag}(.*?){close_tag}"


def get_units_from_url(url=URL):
    resp = urllib.request.urlopen(url)
    html = resp.read().decode()
    units_line = next(line for line in html.splitlines() if open_tag in line)
    blob = re.search(pattern, units_line).group(1)
    return json.loads(blob)


if __name__ == '__main__':
    units = get_units_from_url(url=URL)

    with open(OUT_FILE, 'w') as f:
        f.write(json.dumps(units))


# # todo: implement
#
# import pandas as pd
#
# df = pd.concat([pd.DataFrame(x['AvailableUnits']) for x in units['BedroomTypes']])
# df.sort_values(by=['BuildingId', 'UnitId']).to_csv('table.csv')


# prev:
#    - cron:  '5 0,11,17 * * *'
#    - cron:  '5 * * * *'


