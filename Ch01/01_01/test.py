from pathlib import Path

kb = 2**10

csv_file = Path('.\track.csv')
csv_file.stat().st_size / kb

import pandas as pd

df = pd.read_csv(csv_file)
print(len(df))

