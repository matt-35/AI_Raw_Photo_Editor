# %%
import pandas as pd 
from p_tqdm import p_umap
import os 
from glob import glob

import config 
from read_img import convert_img_to_df_histogram
from read_xmp import read_xmp

# %%
if __name__ == '__main__':

    training_path = 'training_images/Worship/'

    raw_images = glob(f'{training_path}/*.NEF') + glob(f'{training_path}/*.CR2')
    xmp_files = glob(f'{training_path}/*.xmp')

    ## Read raw images.
    img_hist_df = pd.concat(
        p_umap(convert_img_to_df_histogram, raw_images)
    )

    ## Read xmp files
    xmp_df = pd.concat(
        p_umap(read_xmp, xmp_files)
    )
 
    training_df = img_hist_df.join(xmp_df)

    training_df.to_csv('training_data/image_data_worship.csv')

# %%
