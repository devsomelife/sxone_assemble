import sys
from datetime import datetime

import pandas as pd

PADDING = 150

if len(sys.argv) == 1:
    print("Usage: python vsa_prep.py [file_name] [year] [month]")
    print("file_name: Path of the file to process.")
    print("year: The year to filter by. Defaults to the current year if not provided.")
    print("month: The month to filter by. Defaults to the current month if not provided.")
    sys.exit()

file_name = sys.argv[1]

now = datetime.now()
year = now.year if len(sys.argv) < 3 else int(sys.argv[2])
month = now.month if len(sys.argv) < 4 else int(sys.argv[3])

df = pd.read_csv(file_name, delimiter='|', parse_dates=['Date'], dayfirst=True)
df = df[(df['Date'].dt.year == year) & (df['Date'].dt.month == month)]
df['Durée'] = df['Durée'].str.replace(',', '.').astype(float)

df['Durée'] = df['Durée'].replace({0.13: 0.125, 0.38: 0.375, 0.88: 0.875})
df['Société'] = df['Société'].fillna('-')
df = df.groupby(['Société', 'Affaire', 'Ligne d\'affaire'])['Durée'].sum().reset_index()

totalDuration = 0

print("{:=<{}}".format("====[ VSA SUMMARY FOR {}/{} ]====".format(month, year), PADDING))
for index, row in df.iterrows():
    print("{:<20} | {:<20} | [{:<5}] {} ".format(row['Société'], row['Affaire'], row['Durée'], row['Ligne d\'affaire']))
    totalDuration += row['Durée']
print("=" * PADDING)
print("Duration: {}", totalDuration)
