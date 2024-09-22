import spacy
import os
import xml.etree.ElementTree as ET

from spacy import displacy
from aux_func import get_text

files_dir = 'sem-clin-br-xml-filter'

custom_nlp = spacy.load('./output/model-best')
default_nlp = spacy.load('pt_core_news_md')

docs = []

# Teste -Arquivo 01
tree = ET.parse(os.path.join(files_dir, '9849.xml'))
root = tree.getroot()
text = get_text(root)

docs.append(custom_nlp(text))
docs.append(default_nlp(text))

# Teste -Arquivo 02
tree = ET.parse(os.path.join(files_dir, '9840.xml'))
root = tree.getroot()
text = get_text(root)

docs.append(custom_nlp(text))
docs.append(default_nlp(text))

# Teste -Arquivo 03
tree = ET.parse(os.path.join(files_dir, '9858.xml'))
root = tree.getroot()
text = get_text(root)

docs.append(custom_nlp(text))
docs.append(default_nlp(text))


colors = {
    'SINTOMA|SINAL': '#B2DFF7',
    'DOENÇA|SINDROME': '#FFC3A0',
    'PARTE DO CORPO|ORGAO': '#FFABAB',
    'PROCEDIMENTO': '#FF677D',
    'DISPOSITIVO MEDICO': '#D4A5A5',
    'CELULA|DISFUNCAO MOLECULAR': '#392F5A',
    'PROCEDIMENTO DIAGNOSTICO': '#6B4226',
    'FUNCAO FISIOLOGICA': '#FFD166',
    'CONCLUSAO': '#06D6A0',
    'ANTIBIOTICO': '#F9C74F',
    'LOCALIZACAO NO CORPO OU REGIAO': '#84C9FB',
    'RESULTADO LABORATORIO OU TESTE': '#B9FBC0',
    'MEMBRO FAMILIAR': '#F9844A',
    'ACAO DE CUIDADO': '#F0A500',
    'FARMACO|HORMONIO|PROTEINA': '#90BE6D',
    'LESAO': '#F94144',
    'ENVENENAMENTO': '#F3722C',
    'BACTERIA': '#F8961E'
}

options = {'colors': colors}

displacy.serve(docs, style='ent', options=options, host='127.0.0.1')