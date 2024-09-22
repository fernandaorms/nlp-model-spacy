import shutil
import os
import xml.etree.ElementTree as ET

from aux_func import get_text

input_dir = 'sem-clin-br-xml'
output_dir = 'sem-clin-br-xml-filter'

def filter_text(text):
    return ('\n' not in text) and ('\t' not in text)

for filename in os.listdir(input_dir):
    input_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, filename)

    tree = ET.parse(input_path)
    root = tree.getroot()

    text = get_text(root)

    if filter_text(text):
        shutil.copy(input_path, output_path)