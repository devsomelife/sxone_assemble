#!/bin/bash

DEFAULT_FILE_PATH="/app/data.csv"

current_month=$(date +%m)
current_year=$(date +%Y)


param1=${1:-$DEFAULT_FILE_PATH}
param2=${2:-$current_month}
param3=${3:-$current_year}

python sxone_assemble.py "$param1" "$param2" "$param3"
