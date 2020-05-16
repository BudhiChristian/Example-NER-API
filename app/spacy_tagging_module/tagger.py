import spacy

from . import modeLocation

model = None


def refresh():
    global model
    model = spacy.load(modeLocation)


def tag_text(text: str):
    global model
    doc = model(text)
    
    for ent in doc:
        print(ent.label_, ent.text)
