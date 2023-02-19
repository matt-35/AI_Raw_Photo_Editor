# %%
import rawpy
import numpy as np 
from PIL import Image 
import pandas as pd 

def convert_img_to_df_histogram(file_name:str) -> pd.DataFrame:

    raw_data = rawpy.imread(file_name)
    # Convert raw into readable array.
    img = Image.fromarray(raw_data.postprocess())

    # Resize image
    img = img.resize([500,500])

    ## Convert to rgb hisogram.
    r, g, b = img.split()
    r = r.histogram()
    g = g.histogram()
    b = b.histogram()

    ## Convert to datafame 

    image_series = pd.concat([
        pd.Series(r, index=['red_' + str(i) for i in range(256)]),
        pd.Series(g, index=['green_' + str(i) for i in range(256)]),
        pd.Series(b, index=['blue_' + str(i) for i in range(256)])
    ])

    df = pd.DataFrame(image_series).transpose()
    df.index = [file_name.split('/')[-1].split('.')[0]]

    return df 


# %%
if __name__ == '__main__':
    file = 'DSC_0002.NEF'

    df_hist = convert_img_to_df_histogram(file)

# %%
