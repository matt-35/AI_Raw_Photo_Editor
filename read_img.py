# %%
import rawpy
import numpy as np 
from PIL import Image 

# %%

raw_data = rawpy.imread('DSC_0002.NEF')

img = Image.fromarray(raw_data.postprocess())
# %%

img = img.resize([100,100])
# %%

img_arr = np.asarray(img)
# %%

img_arr_flat = img_arr.flatten()
# %%
