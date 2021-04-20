#!/bin/bash
mkdir -p files log
url="https://www.equityapartments.com/washington-dc/gallery-place-mt-vernon-triangle/425-mass-apartments"
now=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# wget $url -O files/$now.html -o log/$now.log
wget $url -O file.html

