import math
import random
import spacy
from spacy.util import minibatch

epochs = 10
batch_size = 10
progress_size = 40

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
                texts, annotations = zip(*batch)
                model.update(texts, annotations, sgd=optimizer, drop=0.35, losses=losses)
                __print_progress((idx*batch_size)+len(batch), len(training_data))
            print('\nLosses', losses)

def __print_progress(current, total):
    num_complete = math.floor(progress_size * (current/total))
    num_remaining = progress_size - num_complete


    progress = ""
    if num_complete > 0:
        progress = ("=" * (num_complete - 1))+">"
    remaining = "_" * num_remaining

    print(f"{current}/{total} complete [{progress}{remaining}]\r", end="")
    

