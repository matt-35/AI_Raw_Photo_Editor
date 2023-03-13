# %%
import pandas as pd 
from p_tqdm import p_umap
import os 
from glob import glob 

import config 
from read_img import image_to_array
from read_xmp import read_xmp

# %%
if __name__ == '__main__':

    training_path = 'training_images/Worship/'

    raw_images = glob(f'{training_path}/*.NEF') + glob(f'{training_path}/*.CR2')
    xmp_files = glob(f'{training_path}/*.xmp')

    ## Read raw images.
    img_arr_df = pd.concat(
        p_umap(image_to_array, raw_images)
    )

    ## Read xmp files
    xmp_df = pd.concat(
        p_umap(read_xmp, xmp_files)
    )

    training_df = img_arr_df.join(xmp_df)

    training_df.to_csv('training_data/image_arr_worship.csv')
# %%
