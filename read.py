# %%
import pandas as pd 
import numpy as np 
import config

def read_xmp(file_name:str) -> pd.DataFrame:

    with open(file_name, 'r') as f:
        meta_list = f.readlines()

    edits_list = [i.strip() for i in meta_list if i.strip().split('=')[0] in ' '.join(config.metadata_edits)]

    edits_list = [i.replace('\"', '') for i in edits_list]

    edits_list = [i.split('=') for i in edits_list]

    df = pd.DataFrame(new_list)
    df[1] = df[1].astype(np.float64)

    df = df.set_index(0).transpose()

    index_name = file_name.split('/')[-1].replace('.xmp','')

    df.index = [index_name]

    return df

# %%

if __name__ == '__main__':
    pass

with open('training_images/5D4_9050.xmp','r') as f:
    meta_list = f.readlines()

# meta_list = [i.strip().replace('crs:','') for i in meta_list if 'crs:' in i]

m_list = [i.strip() for i in meta_list if i.strip().split('=')[0] in ' '.join(config.metadata_edits)]
# %%
# meta_list = [
#  'Version="14.1"',
#  'CompatibleVersion="234881024"',
#  'ProcessVersion="11.0"',
# #  'WhiteBalance="As Shot"',
#  'Temperature="5900"',
#  'Tint="+12"',
#  'Exposure2012="+0.55"',
#  'Contrast2012="+28"',
#  'Highlights2012="-41"',
#  'Shadows2012="+40"',
#  'Whites2012="+4"',
#  'Blacks2012="-28"',
#  'Texture="+24"',
#  'Clarity2012="0"',
#  'Dehaze="0"',
#  'Vibrance="+15"',
#  'Saturation="-8"',
#  'ParametricShadows="0"',
#  'ParametricDarks="0"',
#  'ParametricLights="0"',
#  'ParametricHighlights="0"',
#  'ParametricShadowSplit="25"',
#  'ParametricMidtoneSplit="50"',
#  'ParametricHighlightSplit="75"']

m_list = [i.replace('\"', '') for i in m_list]

new_list = [i.split('=') for i in m_list]


# %%


df = pd.DataFrame(new_list)
df[1] = df[1].astype(np.float64)


df = df.set_index(0).transpose()


# %%
