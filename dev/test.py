# %%
import exiftool

def extract_edits(xmp_file):
    with exiftool.ExifTool() as et:
        metadata = et.get_metadata(xmp_file)
    return metadata['XMP:History']

# %%
edits = extract_edits('DSC_0034.xmp')

# %%
