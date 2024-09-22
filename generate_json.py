import os
import json
import xml.etree.ElementTree as ET

from aux_func import *

input_dir = 'sem-clin-br-xml-filter'
output_dir = 'spacy-json'

train_data = []

sem_clin_files = os.listdir(input_dir)

# Loop para determinar os índices específicos de busca nos arquivos
for i in range(0, 200):
    filename = sem_clin_files[i]
    input_path = os.path.join(input_dir, filename)

    tree = ET.parse(input_path)
    root = tree.getroot()

    text = get_text(root)
    annotations = get_annotations(root)

    train_data.append({'text': text, 'entities': annotations})


with open('./json/clin_data_0_200.json', 'w', encoding='utf-8') as file:
    json.dump(train_data, file, ensure_ascii=False)