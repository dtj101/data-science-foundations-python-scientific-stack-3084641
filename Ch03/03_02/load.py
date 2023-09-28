# %% File size
from pathlib import Path

kb = 2**10

csv_file = Path('track.csv')
csv_file.stat().st_size / kb

# %%
!wsl cat /etc/os-release

# %%
%%gitbash
which bash
cat /etc/os-release

# %%
!wsl ls -lh $csv_file

# %%
%lsmagic

# %% First few lines & line count
count = 0
with csv_file.open() as fp:
    for lnum, line in enumerate(fp, 1):
        count += 1
        if lnum <= 5:
            print(line, end='')
print(f'{count} lines')

# %% First few lines
!head -5 $csv_file

# %% Line count
!wc -l $csv_file

# %% Load to data frame
import pandas as pd

df = pd.read_csv(csv_file)
len(df)

# %%
df.columns
# %%
df.info()
# %%
df.describe()
