# %%
import xml.etree.ElementTree as ET
import pandas as pd

def parse_lightroom_xmp(xml_string):
    # Parse the XMP metadata XML string using ElementTree
    root = ET.fromstring(xml_string)
    
    # Define the XMP namespace and a dictionary to store the metadata
    xmp_ns = {
        'rdf':"http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        'xmp': 'http://ns.adobe.com/xap/1.0/', 
        'crd': 'http://ns.adobe.com/camera-raw-defaults/1.0/',
        'tiff': "http://ns.adobe.com/tiff/1.0/",
        'exif':"http://ns.adobe.com/exif/1.0/",
        'aux':"http://ns.adobe.com/exif/1.0/aux/",
        'photoshop':"http://ns.adobe.com/photoshop/1.0/",
        'xmpMM':"http://ns.adobe.com/xap/1.0/mm/",
        'stEvt':"http://ns.adobe.com/xap/1.0/sType/ResourceEvent#",
        'dc':"http://purl.org/dc/elements/1.1/",
        'crs':"http://ns.adobe.com/camera-raw-settings/1.0/",
    }
    edits = {}

    # Loop through all elements with the XMP namespace
    for element in root.findall('.//rdf:description', xmp_ns):
        print(element)
        # Extract the element name without the namespace
        element_name = element.tag.split('}')[1]
        # Extract the element value
        element_value = element.text.strip() if element.text is not None else ''
        # Add the element to the metadata dictionary
        edits[element_name] = element_value
    
    # Convert the metadata dictionary to a Pandas DataFrame
    edits_df = pd.DataFrame.from_dict(edits, orient='index', columns=['value'])
    
    return edits_df

def write_lightroom_xmp(xml_string, edits_df):
    # Parse the XMP metadata XML string using ElementTree
    root = ET.fromstring(xml_string)
    
    # Define the XMP namespace and a dictionary to store the metadata
    xmp_ns = {'xmp': 'http://ns.adobe.com/xap/1.0/', 'lr': 'http://ns.adobe.com/lightroom/1.0/'}

    # Loop through all elements with the XMP namespace
    for element in root.findall('.//lr:*', xmp_ns):
        # Extract the element name without the namespace
        element_name = element.tag.split('}')[1]
        # Check if the element is in the edits DataFrame
        if element_name in edits_df.index:
            # Update the element value with the corresponding value from the edits DataFrame
            element.text = str(edits_df.loc[element_name]['value'])
    
    # Serialize the updated XMP metadata to a string
    updated_xml_string = ET.tostring(root, encoding='utf-8', method='xml').decode()
    
    return updated_xml_string


# %%

# Example Adobe Lightroom XMP metadata

with open('DSC_0034.xmp' ,'r') as f:
    xmp_metadata = f.read()

# %%
edits_df = parse_lightroom_xmp(xmp_metadata)
print(edits_df)
# %%
