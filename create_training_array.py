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

    training_path = '/Volumes/SSD500/Mercy Raws/'

    raw_images = glob(f'{training_path}/**/*.NEF', recursive=True)\
        + glob(f'{training_path}/**/*.nef', recursive=True)\
        + glob(f'{training_path}/**/*.CR2', recursive=True)\
        + glob(f'{training_path}/**/*.CR3', recursive=True)\
        + glob(f'{training_path}/**/*.cr2', recursive=True)\
        + glob(f'{training_path}/**/*.cr3', recursive=True)\
        + glob(f'{training_path}/**/*.arw', recursive=True)\
        + glob(f'{training_path}/**/*.ARW', recursive=True)

    xmp_files = glob(f'{training_path}/**/*.xmp', recursive=True)

    ## Read raw images.
    img_arr_df = pd.concat(
        p_umap(image_to_array, raw_images)
    )

    ## Read xmp files
    xmp_df = pd.concat(
        p_umap(read_xmp, xmp_files)
    )

    training_df = img_arr_df.join(xmp_df)

    training_df = training_df.sample(frac=1)

    training_df = training_df.dropna(subset=['crs:Temperature'])

    training_df.to_hdf('training_data/image_arr.h5', key='training_df')
# %%
