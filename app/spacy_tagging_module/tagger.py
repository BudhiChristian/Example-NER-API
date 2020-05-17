import spacy

from . import modeLocation

model = None


def refresh():
    global model
    model = spacy.load(modeLocation)


def tag_text(text: str):
    doc = model(text)

    return {
        "sentence": text,
        "entities": transorm(doc.ents)
    }


def transorm(entities):
    entity_list = list()
    for entity in entities:
        entity_list.append({
            'text': entity.text,
            'start': entity.start_char,
            'end': entity.end_char,
            'label': entity.label_
        })
    return entity_list
