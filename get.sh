#!/bin/bash
mkdir -p files log
url="https://www.equityapartments.com/washington-dc/gallery-place-mt-vernon-triangle/425-mass-apartments"
ia="https://web.archive.org/save"
now=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# wget $url -O files/$now.html -o log/$now.log
wget $url -O file.html
#curl -s $ia/$url > /dev/null

#source .venv/bin/activate
python3 save_json.py
cat _file.json | jq '.' > file.json
rm _file.json
