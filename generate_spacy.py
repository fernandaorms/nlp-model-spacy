import spacy
import json
import random

from spacy.tokens import DocBin

nlp = spacy.blank('pt')

with open('./json/clin_data_0_200.json', 'r', encoding='utf-8') as file:
    train_data = json.load(file)

docs = []

def span_overlaps(doc, span):
    for ent in doc.ents:
        if not (span.end <= ent.start or span.start >= ent.end):
            return True
    return False

for entry in train_data:
    text = entry['text']
    entities = entry['entities']

    doc = nlp(text)

    for entity in entities:
        start, end, label, text = entity[:4]

        span = doc.char_span(start, end, label=label)

        if span is not None:
            if not span_overlaps(doc, span):
                doc.ents = list(doc.ents) + [span]

    docs.append(doc)


# : Reorganizar os docs em uma ordem aleatória
random.shuffle(docs)

# Dividir os docs em duas categorias: Train and Dev - Proporção 0.7 = 70/30
cutoff = int(len(docs) * 0.7)
train_docs = docs[:cutoff]
dev_docs = docs[cutoff:]


# Criar e salvar os docs de treinamento
train_docbin = DocBin(docs=train_docs)
train_docbin.to_disk('./spacy/train.spacy')

# Criar e salvar os docs de teste/avaliação
dev_docbin = DocBin(docs=dev_docs)
dev_docbin.to_disk('./spacy/dev.spacy')