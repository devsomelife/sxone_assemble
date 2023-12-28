import sys
from datetime import datetime

import pandas as pd

PADDING = 150

if len(sys.argv) == 1:
    print("Usage: python sxone_assemble.py [file_path] [month] [year].")
    print("\tExample: python sxone_assemble.py /home/user/data.csv 11 2023\n")
    print("file_path: Path of the file. File must be a valid SXONE export, as a CSV with pipe separators.")
    print("month: The month to filter by. Defaults to the current month.")
    print("year: The year to filter by. Defaults to the current year.")
    sys.exit()

file_path = sys.argv[1]

now = datetime.now()
month = now.month if len(sys.argv) < 3 else int(sys.argv[2])
year = now.year if len(sys.argv) < 4 else int(sys.argv[3])

df = pd.read_csv(file_path, delimiter='|', parse_dates=['Date'], dayfirst=True)
df = df[(df['Date'].dt.year == year) & (df['Date'].dt.month == month)]
df['Durée'] = df['Durée'].str.replace(',', '.').astype(float)

df['Durée'] = df['Durée'].replace({0.13: 0.125, 0.38: 0.375, 0.88: 0.875})
df['Société'] = df['Société'].fillna('-')
df = df.groupby(['Société', 'Affaire', 'Ligne d\'affaire'])['Durée'].sum().reset_index()
df['Ligne d\'affaire'] = df['Ligne d\'affaire'].str.replace('\n', '')

totalDuration = 0
print("{:=<{}}".format("====[ VSA SUMMARY FOR {}/{} ]====".format(month, year), PADDING))
for index, row in df.iterrows():
    if not row.isnull().any():
        print("{:<20} | {:<20} | [{:<5}] {} ".format(row['Société'], row['Affaire'], row['Durée'], row['Ligne d\'affaire']))
        totalDuration += row['Durée']
print("=" * PADDING)
print("{:<46} {}".format("Days worked in the selected month: ", totalDuration))
