# %%
import xml.etree.ElementTree as ET
import pandas as pd

def parse_xmp_to_dataframe(xml_string):
    # Parse the XMP metadata XML string using ElementTree
    root = ET.fromstring(xml_string)
    
    # Define the XMP namespace and a dictionary to store the metadata
    xmp_ns = {'xmp': 'http://ns.adobe.com/xap/1.0/'}
    metadata = {}

    # Loop through all elements with the XMP namespace
    for element in root.findall('.//xmp:*', xmp_ns):
        # Extract the element name without the namespace
        element_name = element.tag.split('}')[1]
        # Extract the element value
        element_value = element.text.strip() if element.text is not None else ''
        # Add the element to the metadata dictionary
        metadata[element_name] = element_value
    
    # Convert the metadata dictionary to a Pandas DataFrame
    metadata_df = pd.DataFrame.from_dict(metadata, orient='index', columns=['value'])
    
    return metadata_df

# %%
# Example Adobe XMP metadata
xmp_metadata = '''
<x:xmpmeta xmlns:x="adobe:ns:meta/">
   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
      <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">
         <xmp:CreatorTool>Adobe Photoshop CC 2018 (Windows)</xmp:CreatorTool>
         <xmp:MetadataDate>2019-02-20T13:20:57+02:00</xmp:MetadataDate>
         <xmp:ModifyDate>2019-02-20T13:20:57+02:00</xmp:ModifyDate>
         <xmp:CreateDate>2019-02-20T13:20:57+02:00</xmp:CreateDate>
         <xmp:Rating>3</xmp:Rating>
         <xmp:Label>Green</xmp:Label>
      </rdf:Description>
   </rdf:RDF>
</x:xmpmeta>
'''

with open('DSC_0034.xmp', 'r') as f:
    xmp_metadata = f.read()

# Parse the XMP metadata and convert it to a Pandas DataFrame
metadata_df = parse_xmp_to_dataframe(xmp_metadata)
print(metadata_df)

# %%
