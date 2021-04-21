#!/bin/bash
file="file.json"
sha1sum $file && ./get.sh && sha1sum $file
