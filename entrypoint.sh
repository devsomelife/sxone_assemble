#!/bin/bash

DEFAULT_FILE_PATH="/app/export.xlsx"

current_month=$(date +%m)
current_year=$(date +%Y)


param1=$DEFAULT_FILE_PATH
param2=${1:-$current_month}
param3=${2:-$current_year}

python sxone_assemble.py "$param1" "$param2" "$param3"
