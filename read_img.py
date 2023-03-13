# %%
import rawpy
import numpy as np 
from PIL import Image 
import pandas as pd 
from typing import Tuple

def convert_img_to_df_histogram(file_name:str) -> pd.DataFrame:

    raw_data = rawpy.imread(file_name)
    # Convert raw into readable array.
    img = Image.fromarray(raw_data.postprocess())

    # Resize image
    img = img.resize([1000,1000])

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

    if file_name.endswith('.NEF'):
        df['camera'] = 'Nikon'
    elif file_name.endswith('.CR2'): 
        df['camera'] = 'Canon'

    return df 

def image_to_array(file_name:str, img_size:int=500):

    raw_data = rawpy.imread(file_name)
    img = Image.fromarray(raw_data.postprocess())

    # Resize image
    img = img.resize([img_size,img_size])

    img_arr = np.asarray(img)

    img_name = file_name.split('.')[0]

    df = pd.DataFrame({'img_arr':[img_arr]})
    df.index = [file_name.split('/')[-1].split('.')[0]]

    return df

# %%
if __name__ == '__main__':
    file = 'DSC_0002.NEF'

    df_hist = convert_img_to_df_histogram(file)

    img_array = image_to_array(file)

# %%
