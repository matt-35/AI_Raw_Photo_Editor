# %%
import pandas as pd 
import numpy as np 
import config

def read_xmp(file_name:str) -> pd.DataFrame:

    with open(file_name, 'r') as f:
        meta = f.read()
        xmp_start = meta.find('<rdf:Description')
        xmp_end = meta.find('</rdf:Description')

        # if xmp_start != xmp_end:
        xmp_str = meta[xmp_start:xmp_end+19]
        meta_list = xmp_str.split('\n')

    edits_list = [i.strip() for i in meta_list if i.strip().split('=')[0] in ''.join(config.metadata_edits)]

    edits_list = [i.replace('\"', '') for i in edits_list]

    edits_list = [i.split('=') for i in edits_list]

    df = pd.DataFrame(edits_list)

    ## Testing this to remove duplicate columns
    df = df.drop_duplicates(subset=[0], keep='first')

    df[1] = df[1].astype(np.float64)

    df = df.set_index(0).transpose()

    df = df.drop(columns='')

    index_name = file_name.split('/')[-1].replace('.xmp','')

    df.index = [index_name]

    return df

# %%

if __name__ == '__main__':

    file_name = 'training_images/5D4_9050.xmp'

    df_xmp = read_xmp(file_name)

# %%
