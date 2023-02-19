# %%
import rawpy
import numpy as np 
from PIL import Image 
import pandas as pd 

# %%

file = 'DSC_0002.NEF'

raw_data = rawpy.imread(file)

img = Image.fromarray(raw_data.postprocess())
# %%

img = img.resize([100,100])
# %%

## Convert to rgb hisogram.

r, g, b = img.split()

r = r.histogram()
g = g.histogram()
b = b.histogram()
# %%

image_series = pd.concat([
    pd.Series(r, index=['red_' + str(i) for i in range(256)]),
    pd.Series(g, index=['green_' + str(i) for i in range(256)]),
    pd.Series(b, index=['blue_' + str(i) for i in range(256)])
])

df = pd.DataFrame(image_series).transpose()
df.index = [file.split('.')[0]]
# %%
