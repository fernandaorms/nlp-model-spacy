def get_text(root):
    TEXT = root.find('TEXT')
    return TEXT.text


def get_annotations(root):
    annotations = []

    tags = root.find('TAGS')

    for annotation in tags.findall('annotation'):
        tag = get_mapped_tags(annotation.attrib.get('tag'))
        
        if(not tag):
            continue
        
        start = int(annotation.attrib.get('start'))
        end = int(annotation.attrib.get('end'))
        text = annotation.attrib.get('text')

        annotations.append([start, end, tag, text])

    return annotations


def get_mapped_tags(tagname):
    categories = {'sem_clin': [
        'Sign or Symptom',
        'Disease or Syndrome',
        'Body Part, Organ, or Organ Component',
        'Therapeutic or Preventive Procedure',
        'Medical Device',
        'Cell or Molecular Dysfunction',
        'Diagnostic Procedure',
        'Physiologic Function',
        'Finding',
        'Antibiotic',
        'Body Location or Region',
        'Laboratory or Test Result',
        'Family Group',
        'Health Care Activity',
        'Pharmacologic Substance|Hormone|Amino Acid, Peptide, or Protein',
        'Injury or Poisoning',
        'Bacterium'
    ], 'spacy': [
        'SINTOMA|SINAL',
        'DOENÇA|SINDROME',
        'PARTE DO CORPO|ORGAO',
        'PROCEDIMENTO',
        'DISPOSITIVO MEDICO',
        'CELULA|DISFUNCAO MOLECULAR',
        'PROCEDIMENTO DIAGNOSTICO',
        'FUNCAO FISIOLOGICA',
        'CONCLUSAO',
        'ANTIBIOTICO',
        'LOCALIZACAO NO CORPO OU REGIAO',
        'RESULTADO LABORATORIO OU TESTE',
        'MEMBRO FAMILIAR',
        'ACAO DE CUIDADO',
        'FARMACO|HORMONIO|PROTEINA',
        'LESAO',
        'ENVENENAMENTO',
        'BACTERIA'
    ]}

    if tagname in categories['sem_clin']:
        index = categories['sem_clin'].index(tagname)

        return categories['spacy'][index]

    return ''