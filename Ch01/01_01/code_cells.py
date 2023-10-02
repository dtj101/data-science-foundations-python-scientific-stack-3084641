# %%
import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
40 + 2

# %%
"Hi" + " there"

# %%

xs = np.linspace(-6, 6, 1000)
ys = np.sin(xs)
plt.plot(xs, ys)

# %%

kb = 2**10

csv_file = Path('track.csv')
csv_file.stat().st_size / kb

# %%

df = pd.read_csv(csv_file)
len(df)

# %%
df.columns
# %%
df.info()
# %%
df.describe()
