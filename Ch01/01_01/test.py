import os
from pathlib import Path

kb = 2**10

# cwd = os.getcwd()

# __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
# csv_file = Path(os.path.join(__location__, 'track.csv'))

# print(os.path.dirname(__file__), "track.csv")
# source_file = os.path.dirname(__file__), "track.csv"
# csv_file = Path(source_file)

# csv_file = Path('track.csv')
csv_file = Path(__file__).with_name('track.csv')

csv_file.stat().st_size / kb

import pandas as pd

df = pd.read_csv(csv_file)
print(len(df))

