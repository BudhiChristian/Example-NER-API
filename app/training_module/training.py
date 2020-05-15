import random
import spacy
from spacy.util import minibatch

epochs = 10
batch_size = 10

def train_model(training_data, labels):
    model = spacy.blank('en')

    ner_pipe = model.create_pipe('ner')
    for label in labels:
        ner_pipe.add_label(label)

    model.add_pipe(ner_pipe)

    optimizer = model.begin_training()

    other_pipes = [pipe for pipe in model.pipe_names if pipe != 'ner']
    with model.disable_pipes(*other_pipes):
        for epoch in range(epochs):
            print(f"Epoch {epoch+1}/{epochs}")
            random.shuffle(training_data)
            losses = dict()
            batches = minibatch(training_data, size=batch_size)

            for idx, batch in enumerate(batches):
                print(f"{idx*batch_size}/{len(training_data)}\r", end="")
                texts, annotations = zip(*batch)
                model.update(texts, annotations, sgd=optimizer, drop=0.35, losses=losses)
            print(f"{len(training_data)}/{len(training_data)}")
            print('Losses', losses)
