# %%
from bs4 import BeautifulSoup


# %%
with open('DSC_0002.xmp', 'r') as f:
    meta = f.read()
    xmp_start = meta.find('<rdf:Description')
    xmp_end = meta.find('</rdf:Description')

    # if xmp_start != xmp_end:
    xmp_str = meta[xmp_start:xmp_end+19]
# %%


import requests as re

xmp = re.get('http://DSC_0002.xmp?')
# %%

n = BeautifulSoup(xmp_str, 'html')
# %%
